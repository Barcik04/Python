# pip install aiohttp
import asyncio, aiohttp
from datetime import date, timedelta

CITIES = {
    "Porlamar": (10.96, -63.86),
    "Moroni": (-11.70, 43.25),
    "Helsinki": (60.17, 24.94),
}

DATE = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")  # next day

URL = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude={lat}&longitude={lon}"
    f"&hourly=temperature_2m"
    f"&start_date={DATE}&end_date={DATE}"
    "&timezone=UTC"
)

async def fetch_weather(name, lat, lon):
    async with aiohttp.request("GET", URL.format(lat=lat, lon=lon)) as r:
        j = await r.json()
        hourly = j.get("hourly")
        if not hourly:       # if API didn’t return data for this day
            return name, None
        temps = hourly["temperature_2m"]   # 24 values (0–23)
        avg = sum(temps) / len(temps)
        return name, avg

async def task8():
    tasks = [fetch_weather(n, lat, lon) for n, (lat, lon) in CITIES.items()]
    pairs = await asyncio.gather(*tasks)
    pairs = [(n, a) for n, a in pairs if a is not None]
    pairs.sort(key=lambda x: x[1], reverse=True)
    return dict(pairs)

if __name__ == "__main__":
    result = asyncio.run(task8())
    for city, avg in result.items():
        print(f"{city}: {avg:.1f}°C")
