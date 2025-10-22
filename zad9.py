# pip install aiohttp
import asyncio, aiohttp

# Build 100 URLs (some 500s to trigger retries)
URLS = [
    f"https://httpbin.org/status/{200 if i % 3 else 500}"
    for i in range(100)
]

async def fetch_with_retry(url, max_retries=3):
    for _ in range(max_retries):
        async with aiohttp.request("GET", url) as r:
            if 200 <= r.status < 300:
                return url, r.status
            if 500 <= r.status < 600:
                continue
            return None
    return None

async def main():
    tasks = [fetch_with_retry(u) for u in URLS]
    results = await asyncio.gather(*tasks)
    ok = [x for x in results if x is not None]
    print(ok)

if __name__ == "__main__":
    asyncio.run(main())
