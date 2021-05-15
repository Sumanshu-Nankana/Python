import asyncio

async def main():
    print("hello")
    await asyncio.sleep(2)
    print('World')


asyncio.run(main())