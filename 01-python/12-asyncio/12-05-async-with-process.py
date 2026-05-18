import asyncio
from concurrent.futures import ProcessPoolExecutor

def encrpt(data):
    return f"{data[::-1]}"

async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, encrpt, "hello")
        print(result)

if __name__ == "__main__":
    asyncio.run(main())