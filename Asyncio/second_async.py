import asyncio
import time

async def two():
    print("Starting Two")
    await asyncio.sleep(2)
    print("hey Two")
    return 2
    
async def four():
    print("Starting four")
    await asyncio.sleep(4)
    print("hey four")
    return 4

async def main():
     print(await asyncio.gather(two(), four()))
    
    
start = time.time()
asyncio.run(main())
end = time.time()
print(f"{end-start}")  # Now it will run for 4 second


## we did below changes
# 1 - add async keyword
# 2 - instead of blocking code time.sleep, we use non-blocking code asyncio.sleep
# 3 - when particular function is sleeping and waiting, we use 'await' keyword, to tell it can switch to other task
# 4 - and we use main() funcion
# 5 - to create event loop - we use asyncio.run()
# 6 - asyncio.gather() - returns a future instance and collect the returned values in a order