import aiohttp
import asyncio

async def main():
    url = "https://www.boxofficemojo.com/year/2019/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html_body = await response.read()
            return html_body

html_data = asyncio.run(main())  # return bytes
with open('sites/2019.html', 'w') as f:
    f.write(html_data.decode())  # we need to store str, so decode it.