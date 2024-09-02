from pendulum import datetime

from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.decorators import task_group
from airflow.utils.edgemodifier import Label

from itertools import permutations


# Labels:
# https://airflow.apache.org/docs/apache-airflow/2.1.3/_modules/airflow/example_dags/example_branch_labels.html

# TaskGroups:
# https://www.astronomer.io/docs/learn/task-groups?tab=decorator#define-task-groups

with DAG(
    dag_id="multiple_branch_loop_1", start_date=datetime(2023, 1, 1), schedule=None
):

    def xcom_push(val):
        return val

    def func():
        pass

    def choose(val):
        return f"task_{val}"

    def check_xcom_output_from_first(val, expected_val):
        assert val == expected_val

    for _current_set in permutations("abc"):
        # a -> b -> c
        # a -> c -> b
        # b -> a -> c
        # b -> c -> a
        # c -> a -> b
        # c -> b -> a
        @task_group(
            f"task_group_{_current_set}",
            tooltip=f"Tasks in the order of {_current_set}",
        )
        def tasks():
            _current_name = "".join(_current_set)
            i, j, k = _current_set
            first = PythonOperator(
                task_id=f"first_task_{_current_name}_{i}",
                python_callable=xcom_push,
                op_kwargs={"val": i},
            )
            second = PythonOperator(
                task_id=f"task_{_current_name}_{j}", python_callable=func
            )
            third = PythonOperator(
                task_id=f"task_{_current_name}_{k}", python_callable=func
            )

            first >> Label(f"{i}->{j}") >> second >> Label(f"{j}->{k}") >> third

        tasks()
