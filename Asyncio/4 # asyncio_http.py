# asyncio also use context-switching
# but it uses one thread instead of multiple-thread
# but it's a code which decide when to leave control of running thread

# instead of requests library ; we will use aiohttp
# also we need to replace with ==> async with

# import requests
import time
import aiohttp
import asyncio

URL = 'https://httpbin.org/uuid'

async def fetch(session, url):
    async with session.get(url) as response:
        json_response = await response.json()
        print(json_response['uuid'])
        
async def main():
    async with aiohttp.ClientSession() as session:
        # creating a list of coroutines
        tasks = [fetch(session, URL) for _ in range(100)]
        await asyncio.gather(*tasks)  
        # it will gather a bunch of couroutines and execute together
        # it take a list of tasks, so we use astrick
    
start = time.time()
asyncio.run(main())  # starting the co-routine
end = time.time()
print(f"Total Time: {end - start}")
    

# Took approx 1.4 seconds to hit 100 external requests
# So we can say similar to multithreading or even a little bit faster
# 