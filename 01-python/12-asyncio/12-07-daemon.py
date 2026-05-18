# Daemon threads are background threads that gets closed automatically as soon as main closes
import threading
import time

print("Main thread is started.. ")
def monitor_temp():
    while True:
        print("Monitoring temperature...")
        time.sleep(2)

threading.Thread(target=monitor_temp, daemon=True).start()

print("Main thread is done")