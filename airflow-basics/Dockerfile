FROM  apache/airflow:slim-3.0.2-python3.12 AS base

USER root
ARG AIRFLOW_USER_HOME=/opt/airflow


ENV PYTHONPATH=${AIRFLOW_USER_HOME}
# in a production environment, always fix the package version number
# FROM base AS deps
USER airflow

RUN pip install apache-airflow-providers-microsoft-mssql apache-airflow-providers-amazon --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.0.2/constraints-3.12.txt"


VOLUME /opt/airflow

# FROM airflow AS config
# ref:   https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html
# guide: https://airflow.apache.org/docs/apache-airflow/stable/howto/set-config.html
ENV AIRFLOW__CORE__LOAD_EXAMPLES=False
WORKDIR $AIRFLOW_USER_HOME

COPY simple_auth_manager_passwords.json.generated .

ENTRYPOINT [ "airflow" ]
CMD standalone
