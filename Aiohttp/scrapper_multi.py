import aiohttp
import asyncio


async def fetch(url, session, year):
    async with session.get(url) as response:
            html_body = await response.read()
            return {"body": html_body, "year": year}


async def main(start_year=2020, years_ago=5):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(0, years_ago):
            year = start_year - i
            url = f"https://www.boxofficemojo.com/year/{year}/"
            tasks.append(asyncio.create_task(fetch(url, session, year)))
        pages_content = await asyncio.gather(*tasks)   
        return pages_content
    
    
html_data = asyncio.run(main())  # return bytes
for result in html_data:
    current_year = result['year']
    data = result['body']
    op_file = f'sites/{current_year}.html'
    with open(op_file, 'w') as f:
        f.write(data.decode())  # we need to store str, so decode it.
        
        
# above code run fast
# but, if there are million of requests, then it hit to website very speedly
# and our IP may get BAN
# so, better we need to use the semaphores