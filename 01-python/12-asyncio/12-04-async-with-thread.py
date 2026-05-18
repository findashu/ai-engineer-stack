import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def check_stock(item):
    print(f"Checking stock for {item}")
    time.sleep(3) # blocking operation
    return f"{item} stock: 42"

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, check_stock, "lappy") #
        print(result)

asyncio.run(main())
