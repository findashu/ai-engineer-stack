import asyncio
import threading
import time

def background_worker():
    while True:
        time.sleep(1)
        print(f"Logging system heartbeat")


async def fetch_order():
    await asyncio.sleep(3)
    print("Order fetched")

threading.Thread(target=background_worker, daemon=True).start()

asyncio.run(fetch_order())