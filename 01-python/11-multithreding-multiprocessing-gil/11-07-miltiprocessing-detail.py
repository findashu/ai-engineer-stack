from multiprocessing import Process
import time

def cpu_heavy():
    print("Crunching some numbers...")
    total = 0
    for i in range(10**7):
        total += i
    print(f"Done {total}")

# test this example using threading - You'll notice thread takes more time than multi processing

if __name__ == "__main__":
    start = time.time()
    processes = [Process(target=cpu_heavy) for _ in range(2)]
    [process.start() for process in processes]
    [process.join() for process in processes]
    end = time.time()
    print(f"Time taken: {end - start}")