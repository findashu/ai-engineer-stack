import threading
import time
import requests

def download_img(url):
    print(f"Starting download: {url}")
    response = requests.get(url)
    print(f"Finished download: {url}, size: {len(response.content)} bytes")

urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg"
]

start = time.time()
threads = []

for url in urls:
    t= threading.Thread(target=download_img, args=(url,)) # passing args to target functions using args as tuple
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()
print(f"Total time: {end - start} seconds")