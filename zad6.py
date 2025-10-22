# pip install aiohttp
import asyncio
import aiohttp

CITIES = {
    "Porlamar": (10.96, -63.86),
    "Moroni": (-11.70, 43.25),
    "Helsinki": (60.17, 24.94),
}

URL = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude={lat}&longitude={lon}"
    "&current=temperature_2m,wind_speed_10m"
    "&timezone=UTC"
)

async def fetch_weather(name, lat, lon):
    async with aiohttp.request("GET", URL.format(lat=lat, lon=lon)) as resp:
        data = await resp.json()
        current = data["current"]
        return name, {
            "temperature_2m": current["temperature_2m"],
            "wind_speed_10m": current["wind_speed_10m"]
        }

async def task5():
    tasks = [fetch_weather(name, lat, lon) for name, (lat, lon) in CITIES.items()]
    results = await asyncio.gather(*tasks)
    return dict(results)

if __name__ == "__main__":
    result = asyncio.run(task5())
    for city, data in result.items():
        if data["wind_speed_10m"] > 20:
            print(f"{city}: {data}\n")