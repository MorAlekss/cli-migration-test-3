import requests
BASE_URL = "https://wttr.in"

def get_weather(city):
    response = requests.get(f"{BASE_URL}/{city}?format=j1")
    response.raise_for_status()
    return response.json()

def get_temperature(city):
    data = get_weather(city)
    return data["current_condition"][0]["temp_C"]
