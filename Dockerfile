FROM --platform=linux/amd64 apache/airflow:slim-2.9.1-python3.12 AS base

USER root
ARG AIRFLOW_USER_HOME=/opt/airflow


ENV PYTHONPATH=${AIRFLOW_USER_HOME}
# in a production environment, always fix the package version number
FROM base AS deps
USER airflow

RUN pip install apache-airflow-providers-microsoft-mssql apache-airflow-providers-amazon --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.9.1/constraints-3.12.txt"


FROM deps AS airflow


VOLUME /opt/airflow/dags

FROM airflow AS config
# ref:   https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html
# guide: https://airflow.apache.org/docs/apache-airflow/stable/howto/set-config.html
ENV AIRFLOW__CORE__LOAD_EXAMPLES=False
RUN airflow db init &&\
    airflow users create -e aoeu@aoeu.cc -f aoeu -l aeou -r Admin -u airflow -p airflow

ENTRYPOINT [ "airflow" ]
CMD ["standalone"]
