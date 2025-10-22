# pip install aiohttp
import asyncio
import aiohttp

CITIES = {
    "Porlamar": (10.96, -63.86),
    "Moroni": (-11.70, 43.25),
    "Helsinki": (60.17, 24.94),
}

DATE = "2025-10-25"
HOUR = "11:00"

URL = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude={lat}&longitude={lon}"
    f"&hourly=temperature_2m"
    f"&start_date={DATE}&end_date={DATE}"
    "&timezone=UTC"
)

async def fetch_weather(name, lat, lon):
    async with aiohttp.request("GET", URL.format(lat=lat, lon=lon)) as resp:
        data = await resp.json()
        times = data["hourly"]["time"]
        temps = data["hourly"]["temperature_2m"]
        target = f"{DATE}T{HOUR}"
        temp = temps[times.index(target)]
        return name, temp

async def task5():
    tasks = [fetch_weather(n, lat, lon) for n, (lat, lon) in CITIES.items()]
    results = await asyncio.gather(*tasks)
    return dict(results)

if __name__ == "__main__":
    result = asyncio.run(task5())
    for city, temp in result.items():
        print(f"{city}: {temp}\n")
