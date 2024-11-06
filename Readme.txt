1. create a directory named airflow and inside that create three sub directories - logs, dags, plugins and place docker-compose.yaml file inside airflow directory
2. install docker desktop for windows
3. download docker-compose.yaml file of airflow latest release
https://airflow.apache.org/docs/apach...

Airflow releases: https://airflow.apache.org/docs/apach...

4. docker-compose up airflow-init
5. docker-compose up

Cleanup - below command will delete all the conainer and free up the volumes and memory
`Run docker-compose down --volumes --remove-orphans`
command in the directory you downloaded the docker-compose.yaml file

airflow-scheduler - The scheduler monitors all tasks and DAGs, then triggers the task instances once their dependencies are complete.
airflow-webserver - The webserver is available at http://localhost:8080.
airflow-worker - The worker that executes the tasks given by the scheduler.
airflow-triggerer - The triggerer runs an event loop for deferrable tasks.
airflow-init - The initialization service.
postgres - The database.
redis - The redis - broker that forwards messages from scheduler to worker.