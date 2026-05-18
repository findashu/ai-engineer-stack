from multiprocessing import Process
import time

def cook_food(name):
    print(f"Starting to cook food {name}")
    time.sleep(3)  # Simulate cooking time
    print(f"Finished cooking food {name}")

if __name__ == "__main__":
    # creating array of process, with targets and args
    cooks = [Process(target=cook_food, args=(f"Food {i+1}",)) for i in range(3)]

    # Start all process
    for p in cooks:
        p.start()
    # wait for all to complete
    for p in cooks:
        p.join()

    print("All foods cooked.")