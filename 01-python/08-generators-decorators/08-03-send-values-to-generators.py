def take_order():
    print("Welcome, What would you like to order?")
    order = yield # Program stops on first run as it waits for a value to be sent
    while True:
        print(f"You ordered: {order}")
        order = yield # Stopping the loop, waits for value once recived go through the loop

stall = take_order()
next(stall)  # Start the generator
stall.send("Burger")  # Send a value to the generator
stall.send("Fries")  # Send another value to the generator