import aiohttp
import asyncio


async def fetch(url, session, year=None):
    async with session.get(url) as response:
            html_body = await response.read()
            return {"body": html_body, "year": year}


async def fetch_with_sem(url, session, sem, year):
    async with sem:
        return await fetch(url, session, year)


async def main(start_year=2020, years_ago=5):
    tasks = []
    
    # Semaphore
    sem = asyncio.Semaphore(10)  # In bracker we have the limit i.e. how many requests can run at given time
    
    async with aiohttp.ClientSession() as session:
        for i in range(0, years_ago):
            year = start_year - i
            url = f"https://www.boxofficemojo.com/year/{year}/"
            tasks.append(asyncio.create_task(fetch_with_sem(url, session, sem, year)))
        pages_content = await asyncio.gather(*tasks)   
        return pages_content
    
    
html_data = asyncio.run(main())  # return bytes
for result in html_data:
    current_year = result['year']
    data = result['body']
    op_file = f'sites/{current_year}.html'
    with open(op_file, 'w') as f:
        f.write(data.decode())  # we need to store str, so decode it.
        
        