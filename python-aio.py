import http.client
import aiohttp
import asyncio
import time

async def main():
    start = time.time()
    host = 'http://localhost:3000'
    async with aiohttp.request('GET', host) as resp:
        txt = await resp.text()
    end = time.time()
    print(end - start)
    return txt

asyncio.run(main())