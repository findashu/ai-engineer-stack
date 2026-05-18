from multiprocessing import Process, Queue, Value

def chef(queue):
    queue.put("Preparing food")

def increment(counter):
    for _ in range(10000):
        with counter.get_lock():
            counter.value += 1

if __name__ == "__main__":
    queue = Queue()
    p = Process(target=chef, args=(queue,))
    p.start()
    p.join()
    print(queue.get())
    counter = Value('i', 0) # i with default value 0
    valueProcesses = [Process(target=increment, args=(counter,)) for _ in range(4)]
    [pr.start() for pr in valueProcesses]
    [pr.join() for pr in valueProcesses]
    print(f"Counter value: {counter.value}")