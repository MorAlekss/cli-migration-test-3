import sys
import asyncio
from src.weather import get_temperature
from src.news import get_top_stories
from src.geo import geocode
from src.currency import convert

async def main():
    if len(sys.argv) < 2:
        print("Usage: cli <command>")
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "weather":
        print(await get_temperature(sys.argv[2]))
    elif cmd == "news":
        for s in await get_top_stories():
            print(s)
    elif cmd == "geo":
        print(await geocode(sys.argv[2]))
    elif cmd == "convert":
        print(await convert(float(sys.argv[2]), sys.argv[3], sys.argv[4]))

if __name__ == "__main__":
    asyncio.run(main())
