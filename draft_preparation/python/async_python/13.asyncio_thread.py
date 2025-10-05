# asyncio.to_thread - method for running sync tasks inside a async function
import time
import asyncio

def blocking_io():
    time.sleep(1)
    return "Done!!!"

async def main():
    res = await asyncio.to_thread(blocking_io)
    print(res)

asyncio.run(main())

