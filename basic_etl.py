import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

base_url = "https://api.openweathermap.org/data/2.5/forecast"

# 1. Extract
def extract_data(city):
    url = f"{base_url}?q={city}&appid={api_key}"
    response = requests.get(url)
    

# 2. Transform
def transform_data(data):
    transformed_data = {
        "city": data["city"]["name"],
        "temperature": data["list"][0]["main"]["temp"],
        "description": data["list"][0]["weather"][0]["description"]
    }
    return transformed_data

# 3. Load data
def load_data(data, filename):
    df = pd.DataFrame([data])
    df.to_csv(filename, index=False)

# Run the data pipeline
def run_etl_pipeline(city):
    data = extract_data(city)
    transformed_data = transform_data(data)
    load_data(transformed_data, "weather_data.csv")

city = "Pune"
run_etl_pipeline(city)
