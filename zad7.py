
import asyncio, aiohttp

async def download():
    url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/Fronalpstock_big.jpg"
    path = r"C:\Users\igorb\PycharmProjects\pythonProject1\file.jpg"
    async with aiohttp.request("GET", url) as r:
        with open(path, "wb") as f:
            f.write(await r.read())

asyncio.run(download())
