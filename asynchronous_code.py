import aiohttp
import asyncio
import time

number_of_requests = 50
url = "https://jsonplaceholder.typicode.com/posts/"

async def fetch_post(post_num):
    async with aiohttp.ClientSession() as session:
        post_url = url + str(post_num)
        print(f"Hitting Get Request for {post_num} Post")
        async with session.get(post_url) as response:
            return await response.text()

if __name__ == "__main__":
    async def run():
        tasks = []
        for i in range(1, number_of_requests+1):
            tasks.append(fetch_post(i))
        responses = await asyncio.gather(*tasks)
        return responses

    start_time = time.time()
    loop = asyncio.get_event_loop()
    responses = loop.run_until_complete(run())
    end_time = time.time()

    print(f"Asynchronous Execution Time: {end_time - start_time}")
