import asyncio
import time

async def display_time():
    start = time.time()
    
    while True:
        dur = int(time.time() - start)
        if dur % 3 == 0:
            print(f"{dur} seconds have passed")
        
        await asyncio.sleep(1)
        
        
async def print_num():
    num = 1
    
    while True:
        print(num)
        num += 1
        await asyncio.sleep(0.1)
        
        
async def main():
    task1 = asyncio.create_task(display_time())
    task2 = asyncio.create_task(print_num())
    await asyncio.gather(task1, task2)

asyncio.run(main())

# instead of create_task ==> we can use ensure_future