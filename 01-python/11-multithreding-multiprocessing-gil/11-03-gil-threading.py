import threading
import time

def brew_coffee():
    print(f"{threading.current_thread().name} is started brewing coffee.")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} has finished brewing coffee.")

thread1 = threading.Thread(target=brew_coffee, name="Thread-1")
thread2 = threading.Thread(target=brew_coffee, name="Thread-2")

start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()

print(f"Total time taken: {end - start:.2f} seconds")