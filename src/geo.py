import httpx
BASE_URL = "https://nominatim.openstreetmap.org"

async def geocode(address):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/search", params={"q": address, "format": "json"})
        response.raise_for_status()
        return response.json()

async def reverse_geocode(lat, lon):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/reverse", params={"lat": lat, "lon": lon, "format": "json"})
        response.raise_for_status()
        return response.json()
