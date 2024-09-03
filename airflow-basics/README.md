# Airflow basics
The material in this section (kata) is intended to provide a basic understanding of Apache Airflow. The exercises are designed to be completed in order, as they build on each other.

You should set aside 1-3 hours to complete the exercises and get familiar with the documentation, tooling and concepts.

## Pre-requisites
- text editor
- Docker (and optionally docker compose)
- web browser 

## 🧠 Exercises
1. Run Airflow in a Docker container and log-in
1. Enable the example DAGs and run one
1. Create a new DAG that prints "Hello, World!" to the logs
1. Create a new dynamic DAG. The dag should create all permutations of `[a, b, c]` tasks.
1. Modify the previously created DAG to always skip the task `c` if it comes after taks `a`.
1. Create a new DAG that queries data from a server 
    1. Set up docker compose to also run a database alongside Airflow (this requires docker-compose)
    1. Create the connection in the Airflow UI
    1. Create a new DAG that queries data from the database

## 💡 Hints
### Docker

`docker build -t airflow-ds:latest .`

`docker run -it -p 8080:8080 airflow-ds:latest --volume ./dags:/opt/airflow/dags`

*with compose:*
`docker compose up -d`


### Airflow
#### with a pre-configure user
log in: `airflow`
password: `airflow`
#### without configuring a new user
log in: admin
password: `cat standalone_admin_password.txt`


