import requests
import psycopg2
from psycopg2.extras import execute_values

def fetch_data():
    # Example API: Fetching random user data
    url = "https://randomuser.me/api/?results=10"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["results"]
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

def transform_data(raw_data):
    # Extract only the relevant fields from the API response
    transformed_data = [
        (
            user["name"]["first"],
            user["name"]["last"],
            user["email"],
            user["dob"]["age"]
        ) for user in raw_data
    ]
    return transformed_data

def load_data_to_db(data):
    # Database connection parameters
    conn = psycopg2.connect(
        dbname="airflow",
        user="airflow",
        password="airflow",
        host="postgres"
    )
    cursor = conn.cursor()
    
    # Create a table if it does not exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            email VARCHAR(100),
            age INT
        )
    """)
    
    # Insert data into the table
    execute_values(cursor, "INSERT INTO users (first_name, last_name, email, age) VALUES %s", data)
    
    # Commit and close the connection
    conn.commit()
    cursor.close()
    conn.close()

def etl_process():
    raw_data = fetch_data()
    transformed_data = transform_data(raw_data)
    load_data_to_db(transformed_data)

if __name__ == "__main__":
    etl_process()
