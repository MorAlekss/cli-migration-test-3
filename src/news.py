import httpx
BASE_URL = "https://hacker-news.firebaseio.com/v0"

async def get_top_stories():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/topstories.json")
        response.raise_for_status()
        return response.json()[:10]

async def get_story(story_id):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/item/{story_id}.json")
        response.raise_for_status()
        return response.json()
