import asyncio

async def say_hello(name):
    print(f"Hello, {name}!")
    await asyncio.sleep(1)
    print(f"Goodbye, {name}!")

async def main():
    await asyncio.gather(
        say_hello("Alice"),
        say_hello("Bob"),
        say_hello("Charlie"),
    )

asyncio.run(main())
