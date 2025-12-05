import requests
import sqlite3
from config import AVIATIONSTACK_API_KEY

def get_flight_data():
    
    url = "http://api.aviationstack.com/v1/flights"
    
    params = {
        "access_key": AVIATIONSTACK_API_KEY,
        "limit": 25
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    
    data = response.json()
    return data

def calculate_travel_time(cur):
    pass

def visualize_flight_time(data):
    pass


if __name__ == "__main__":
    flights = get_flight_data()
    print(flights) #change later, just making sure it works