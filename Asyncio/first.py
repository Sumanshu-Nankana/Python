import asyncio

async def main():
    print('Hello')
    await asyncio.sleep(1)
    print('World')

asyncio.run(main())   ## This automatically starts the event loop

# we should not use Blocking Code in asynchrouns Programme
# i.e. time.sleep() etc ; if we use it it will make it synchrouns.

# So we have to use Non-Blocking Code, asyncio provides corresponding function
# like asyncio.sleep is same as of time.sleep