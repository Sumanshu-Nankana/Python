import asyncio

async def method1():
    print("hello world 1")
    
loop = asyncio.get_event_loop()
loop.run_until_complete(method1())
loop.close()


async def method2():
    print("hello world 2")
    
asyncio.run(method2())