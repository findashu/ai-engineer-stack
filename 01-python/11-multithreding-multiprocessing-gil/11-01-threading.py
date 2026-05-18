import threading
import time

def take_order():
    for i in range(1,4):
        print(f"Taking order for table #{i}")
        time.sleep(2)  # to Simulate time taking process

def cook_food():
    for i in range(1,4):
        print(f"Cooking food for table #{i}")
        time.sleep(3)  # to Simulate time cooking process


# creating a thread

order_thread = threading.Thread(target=take_order)
cook_thread = threading.Thread(target=cook_food)

# start the thread

order_thread.start()
cook_thread.start()

# Wait for process to complete - join()
order_thread.join()
cook_thread.join()

print(f"All orders processed.")