import time
import asyncio
#import requests
import aiohttp

async def download_file(url):
    print(f"Started Downloading {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            content = await resp.read()
            print(f"Finished Downloading {url}")
            return content

async def write_file(n, content):
    filename = f'sites/sync_{n}.html'
    with open(filename, 'wb') as f:
        print(f"Started writing {filename}")
        f.write(content)
        print(f"Finished writing {filename}")
        
async def scrape_tasks(n, url):
    content = await download_file(url)
    await write_file(n, content)

async def main():
    tasks = []
    # it create a list of tasks havin coroutines
    for n, url in enumerate(open('urls.txt').readlines()):
        tasks.append(scrape_tasks(n, url))
    await asyncio.wait(tasks)

if __name__ == "__main__":
    t = time.perf_counter()
    asyncio.run(main())
    t2 = time.perf_counter() - t
    print(f"Total Time taken {t2:0.2f} seconds")
    
# It just took approx 1.17 seconds
    