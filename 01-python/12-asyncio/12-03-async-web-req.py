import asyncio
import aiohttp

async def fetch(session,url):
    async with session.get(url) as response:
        print(f"Response from {url}: {response.status}")


async def main():
    urls = ["https://httpbin.org/delay/2"] * 3 # List of URLs to fetch
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        await asyncio.gather(*tasks) # *tasks: shorthand to unpack array


asyncio.run(main())