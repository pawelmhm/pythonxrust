import asyncio
import aiohttp
import time

async def fetch(url, session):
    async with session.get(url) as response:
        return await response.text()

async def run_requests(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(url, session) for url in urls]
        responses = await asyncio.gather(*tasks)
        return responses

# Entry point to run the async code
if __name__ == "__main__":
    start = time.time()
    urls = ["http://localhost:3000" for _ in range(10)]  # Replace with your desired URLs
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(run_requests(urls))
    end = time.time()
    print(end - start)
