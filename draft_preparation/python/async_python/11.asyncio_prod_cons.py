import asyncio
import random

async def producer(queue):
    for i in range(10):
        await asyncio.sleep(0.2)  # simulate I/O
        item = random.randint(1, 100)
        await queue.put(item)
        print(f"[Producer] produced {item}")
    await queue.put(None)  # sentinel
    print("[Producer] done")

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        await asyncio.sleep(0.1)  # simulate processing
        print(f"[Consumer] processed {item} -> {item * item}")

async def main():
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))
    print("All done!")

asyncio.run(main())
