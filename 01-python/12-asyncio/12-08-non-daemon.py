# Non Daemon threads will keep on running even main thread closed
import threading
import time

print("Main thread is started.. ")
def monitor_temp():
    while True:
        print("Monitoring temperature...")
        time.sleep(2)

threading.Thread(target=monitor_temp).start()

print("Main thread is done")