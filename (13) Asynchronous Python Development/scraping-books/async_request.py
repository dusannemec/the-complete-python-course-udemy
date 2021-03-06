import aiohttp
import asyncio
import time


async def fetch_page(url):
    page_start = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f'The page took {time.time() - page_start}')
            return response.status


loop = asyncio.get_event_loop()
tasks = [fetch_page('https://google.com') for i in range(50)]
start = time.time()
loop.run_until_complete(asyncio.gather(*tasks))
print(f'All took {time.time() - start}')
