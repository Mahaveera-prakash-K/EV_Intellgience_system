import requests
import pandas as pd
from .config import EV_API_URL

def fetch_ev_data():

    print("Connecting to EV dataset API...")

    response = requests.get(EV_API_URL)

    if response.status_code != 200:
        raise Exception("Failed to fetch data from API")

    data = response.json()

    df = pd.DataFrame(data)

    print("Dataset downloaded successfully")

    return df