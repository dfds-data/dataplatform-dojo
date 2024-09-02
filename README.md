# Docker

docker build -t airflow-ds:latest .
docker run -it -p 8080:8080 airflow-ds:latest --volume ./dags:/opt/airflow/dags

## with compose:
docker compose up -d


# Airflow
log in: admin
password: `cat standalone_admin_password.txt`


