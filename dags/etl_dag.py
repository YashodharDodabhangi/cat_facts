from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import etl_code  # Import the ETL script

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1
}

# Define the DAG
with DAG(
    'etl_dag',
    default_args=default_args,
    schedule_interval='@daily',  # Run daily
    catchup=False
) as dag:

    etl_task = PythonOperator(
        task_id='run_etl',
        python_callable=etl_code.etl_process
    )

etl_task
