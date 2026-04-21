import requests
BASE_URL = "https://nominatim.openstreetmap.org"

def geocode(address):
    response = requests.get(f"{BASE_URL}/search", params={"q": address, "format": "json"})
    response.raise_for_status()
    return response.json()

def reverse_geocode(lat, lon):
    response = requests.get(f"{BASE_URL}/reverse", params={"lat": lat, "lon": lon, "format": "json"})
    response.raise_for_status()
    return response.json()
