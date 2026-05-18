import asyncio

print("Start the program")
async def brew_coffee():
    print("Starting to brew coffee...")
    await asyncio.sleep(3)  # Simulate time taken to brew coffee
    print("Coffee is ready!")

asyncio.run(brew_coffee())
print("Program finished.")
