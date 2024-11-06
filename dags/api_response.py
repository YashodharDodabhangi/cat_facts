import requests

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
