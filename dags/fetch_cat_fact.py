from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import requests

def fetch_cat_fact():
    # Define the URL for the Cat Fact API
    url = "https://catfact.ninja/fact"

    # Make a GET request to the API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Extract the cat fact and its length
        cat_fact = data.get("fact", "No fact found.")
        fact_length = data.get("length", 0)
        
        # Print the cat fact and its length
        print(f"Cat Fact: {cat_fact}")
        print(f"Length of Fact: {fact_length} characters")
    else:
        print(f"Failed to fetch data: {response.status_code} - {response.text}")

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 11, 5),
    'retries': 1,
}

# Create the DAG
dag = DAG('cat_fact_dag', default_args=default_args, schedule_interval='@daily')

# Define the PythonOperator
fetch_fact_task = PythonOperator(
    task_id='fetch_cat_fact',
    python_callable=fetch_cat_fact,
    dag=dag,
)

fetch_fact_task
