import threading
import time

counter = 0
lock = threading.Lock()
def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(5)]

[thread.start() for thread in threads]
[thread.join() for thread in threads]

print(f"Counter: {counter}")