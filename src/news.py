import requests
BASE_URL = "https://hacker-news.firebaseio.com/v0"

def get_top_stories():
    response = requests.get(f"{BASE_URL}/topstories.json")
    response.raise_for_status()
    return response.json()[:10]

def get_story(story_id):
    response = requests.get(f"{BASE_URL}/item/{story_id}.json")
    response.raise_for_status()
    return response.json()
