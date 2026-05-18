import asyncio
import time

async def get_data(name):
    print(f"Fetching data for {name}...")
    await asyncio.sleep(2)  # Simulate delay using await - will not block
    #time.sleep(2) # without await will be blocked
    print(f"Data for {name} is ready!")

async def main():
    await asyncio.gather(
        get_data("Alice"),
        get_data("Bob"),
        get_data("Charlie")
    )

asyncio.run(main())
print("All data fetched.")