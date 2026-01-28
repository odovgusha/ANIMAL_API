import os
import requests
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.api-ninjas.com/v1/animals"

def fetch_data(animal_name):
    """
    Fetch animal data from API for a given animal name.
    Returns a list of dictionaries.
    """
    if not API_KEY:
        print("Error: API_KEY not found in .env")
        return []

    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}

    try:
        response = requests.get(BASE_URL, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()  # returns a list of dictionaries
        else:
            print(f"Error: API returned status {response.status_code}")
            return []
    except requests.RequestException as e:
        print(f"Error: Could not connect to API. {e}")
        return []
