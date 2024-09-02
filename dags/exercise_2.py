from pendulum import datetime

from airflow.models import DAG
from airflow.operators.python import BranchPythonOperator, PythonOperator
from airflow.utils.trigger_rule import TriggerRule


with DAG(dag_id="multiple_branch_loop", start_date=datetime(2023, 1, 1), schedule=None):
    def xcom_push(val):
        return val

    def func():
        ...

    def choose(val):
        return f"task_{val}"

    def check_xcom_output_from_first(val, expected_val):
        assert val == expected_val

    stuff = ["a", "b", "c"]
    for i in stuff:
        first = PythonOperator(task_id=f"first_task_{i}", python_callable=xcom_push, op_kwargs={"val": i})
        branch = BranchPythonOperator(task_id=f"branch_{i}", python_callable=choose, op_kwargs={"val": i})
        second = PythonOperator(task_id=f"task_{i}", python_callable=func)
        third = PythonOperator(task_id=f"task_{i}a", python_callable=func)
        check = PythonOperator(
            task_id=f"check_{i}",
            trigger_rule=TriggerRule.ALL_DONE,
            python_callable=check_xcom_output_from_first,
            op_kwargs={"val": first.output, "expected_val": i},
        )

        first >> branch >> [second, third] >> check
