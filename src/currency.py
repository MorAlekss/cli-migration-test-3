import httpx
BASE_URL = "https://open.er-api.com/v6"

async def get_rates(base="USD"):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/latest/{base}")
        response.raise_for_status()
        return response.json()["rates"]

async def convert(amount, from_currency, to_currency):
    rates = await get_rates(from_currency)
    return amount * rates[to_currency]
