import requests
BASE_URL = "https://open.er-api.com/v6"

def get_rates(base="USD"):
    response = requests.get(f"{BASE_URL}/latest/{base}")
    response.raise_for_status()
    return response.json()["rates"]

def convert(amount, from_currency, to_currency):
    rates = get_rates(from_currency)
    return amount * rates[to_currency]
