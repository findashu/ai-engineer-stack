# Python Asyncio — Asynchronous Programming

A practical guide covering coroutines, the event loop, concurrency patterns, executors, threading edge cases, and when to use what.

---
 
## Table of Contents
 
1. [The Problem Async Solves](#1-the-problem-async-solves)
2. [Core Concepts](#2-core-concepts)
3. [Coroutines — `async def` and `await`](#3-coroutines--async-def-and-await)
4. [Running Multiple Coroutines — `asyncio.gather()`](#4-running-multiple-coroutines--asynciogather)
5. [Real-World I/O — Async HTTP with `aiohttp`](#5-real-world-io--async-http-with-aiohttp)
6. [Mixing Async with Blocking Code — Executors](#6-mixing-async-with-blocking-code--executors)
7. [Background Workers and Daemon Threads](#7-background-workers-and-daemon-threads)
8. [Deadlocks](#8-deadlocks)
9. [Profiling Async Code](#9-profiling-async-code)
10. [Comparison: asyncio vs threading vs multiprocessing](#10-comparison-asyncio-vs-threading-vs-multiprocessing)
11. [Common Pitfalls Cheatsheet](#11-common-pitfalls-cheatsheet)
---

## 1. The Problem Async Solves
 
Imagine your app needs to fetch data from 100 URLs. Three approaches:
 
**Sequential (naive):**
```
Fetch URL 1 → wait 200ms → Fetch URL 2 → wait 200ms → ... × 100
Total: ~20 seconds
```
 
**Threading:**
```
100 threads, each fetching one URL concurrently
Total: ~200ms — but 100 threads is heavy; OS overhead is real
```
 
**Async (asyncio):**
```
1 thread, 100 coroutines — while one waits for a response, others run
Total: ~200ms — same speed as threading, tiny memory footprint

```
 
Asyncio wins in high-concurrency I/O scenarios because it avoids the overhead of creating and managing hundreds of threads. The trade-off: it only helps with **I/O-bound** work. CPU-heavy tasks still need `multiprocessing`.
 
---

## 2. Core Concepts
 
### Coroutine
 
A **coroutine** is a special function defined with `async def` that can pause its execution at `await` points and resume later. Unlike a regular function that runs start-to-finish without interruption, a coroutine can yield control back to the event loop while waiting — letting other coroutines run in the meantime.
 
```python
async def my_coroutine():    # This is a coroutine function
    await asyncio.sleep(1)   # Pause here, let others run
    return "done"
 
# Calling it does NOT run it — it creates a coroutine object
obj = my_coroutine()         # <coroutine object at 0x...>
 
# To actually run it:
asyncio.run(my_coroutine())  # Runs it to completion
```
### `await`
 
`await` does two things:
1. Pauses the current coroutine until the awaited operation completes
2. Returns control to the event loop so other coroutines can run
You can only use `await` inside an `async def` function. Trying to use it in a regular function is a syntax error.
 
```python
# ✅ Correct
async def fetch():
    await asyncio.sleep(2)
 
# ❌ SyntaxError
def fetch():
    await asyncio.sleep(2)
```

**Critical:** `await` only yields control if the thing you're awaiting is actually async. `time.sleep()` is synchronous — it blocks the entire event loop even inside an async function.
 
```python
import time, asyncio
 
async def bad():
    time.sleep(3)        # ❌ Blocks the ENTIRE event loop for 3 seconds
 
async def good():
    await asyncio.sleep(3)  # ✅ Pauses this coroutine, others keep running
```

### Event Loop
 
The **event loop** is the engine that drives async code. It maintains a queue of coroutines and tasks, runs them one at a time, and switches between them whenever one hits an `await`. There is only one event loop per thread, and it runs until all tasks complete.
 
```
Event loop tick:
  1. Run coroutine A until it hits await
  2. Switch to coroutine B, run until it hits await
  3. Switch to coroutine C, run until it hits await
  4. Check if A's await is done → resume A
  ... repeat
```
 
`asyncio.run(coroutine)` is the standard entry point — it creates a new event loop, runs the coroutine to completion, then shuts the loop down.
 
---

## 3. Coroutines — `async def` and `await`
 
### Example: Single Coroutine
 
```python
# 12-01-basic-async.py
import asyncio
 
print("Start the program")
 
async def brew_coffee():
    print("Starting to brew coffee...")
    await asyncio.sleep(3)        # Non-blocking wait — event loop can do other work
    print("Coffee is ready!")
 
asyncio.run(brew_coffee())        # Blocking from the outside — returns only when done
print("Program finished.")
```
 
Output:
```
Start the program
Starting to brew coffee...
  ... (3 seconds pass)
Coffee is ready!
Program finished.
```
 
**Why does `Program finished.` come last?**
 
`asyncio.run()` is a blocking call from the perspective of the caller. It starts the event loop, runs the coroutine to completion, shuts the loop down, and *then* returns. The line after it cannot run until all of that is done.
 
This is different from JavaScript where the event loop is always running in the background. In Python, the loop only exists for the lifetime of `asyncio.run()`.
 
---

## 4. Running Multiple Coroutines — `asyncio.gather()`
 
A single coroutine with one `await` doesn't demonstrate the power. The real benefit shows when multiple coroutines run concurrently.
 
### `asyncio.gather()` — Run Concurrently, Wait for All
 
`asyncio.gather(*coroutines)` starts all the given coroutines, lets them interleave at their `await` points, and returns when **all** of them are done. The results come back in the same order you passed the coroutines, regardless of which finished first.
 
```python
# 12-02-run-multiple-routine.py
import asyncio
import time
 
async def fetch_users():
    print("Fetching users...")
    await asyncio.sleep(2)         # Simulates a 2s DB/API call
    print("Users ready!")
    return ["Alice", "Bob"]
 
async def fetch_orders():
    print("Fetching orders...")
    await asyncio.sleep(1)         # Simulates a 1s DB/API call
    print("Orders ready!")
    return [101, 102, 103]
 
async def fetch_inventory():
    print("Fetching inventory...")
    await asyncio.sleep(3)         # Simulates a 3s DB/API call
    print("Inventory ready!")
    return {"item_A": 50}
 
async def main():
    start = time.time()
    users, orders, inventory = await asyncio.gather(
        fetch_users(),
        fetch_orders(),
        fetch_inventory()
    )
    print(f"All data fetched in {time.time() - start:.1f}s")
    print(users, orders, inventory)
 
asyncio.run(main())
```
 
Output:
```
Fetching users...
Fetching orders...
Fetching inventory...
Orders ready!       ← after 1s
Users ready!        ← after 2s
Inventory ready!    ← after 3s
All data fetched in 3.0s
```
 
Without `gather`, running sequentially would take 2+1+3 = **6 seconds**. With `gather`: **3 seconds** — the slowest one determines total time.

### `create_task()` — Fire and Forget (with care)
 
`asyncio.create_task()` schedules a coroutine to run in the background immediately — without waiting for it right then. Useful when you want to kick off work and collect results later.
 
```python
async def main():
    task = asyncio.create_task(fetch_orders())   # Starts running immediately
    # ... do other work here ...
    result = await task                           # Collect result when needed
```
 
> **Gotcha:** Don't lose the reference to a task. If the task object is garbage collected before it completes, Python will cancel it with a warning.
 
---

## 5. Real-World I/O — Async HTTP with `aiohttp`
 
The standard `requests` library is synchronous — calling `requests.get()` inside an async function blocks the entire event loop until the response arrives. For real async HTTP, use `aiohttp`.
 
```python
# 12-03-async-web-req.py
import asyncio
import aiohttp
import time
 
URLS = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
    "https://jsonplaceholder.typicode.com/posts/4",
    "https://jsonplaceholder.typicode.com/posts/5",
]
 
async def fetch(session, url):
    async with session.get(url) as response:    # async with — non-blocking request
        data = await response.json()            # await the response body too
        print(f"Got post: {data['id']} - {data['title'][:30]}")
        return data
 
async def main():
    start = time.time()
 
    async with aiohttp.ClientSession() as session:   # Reuse one session for all requests
        results = await asyncio.gather(
            *[fetch(session, url) for url in URLS]   # All 5 requests fire concurrently
        )
 
    print(f"\nFetched {len(results)} posts in {time.time() - start:.2f}s")
 
asyncio.run(main())
```
 
**Key patterns here:**
 
- `async with aiohttp.ClientSession()` — the session manages connection pooling; always reuse one session rather than creating one per request
- `async with session.get(url)` — the `async with` ensures the response is properly closed even if an exception occurs
- `await response.json()` — reading the body is also async (it's another I/O operation)
**Setup:**
```bash
pip install aiohttp
python3 12-03-async-web-req.py
```
 
---
 
## 6. Mixing Async with Blocking Code — Executors
 
### The Problem
 
Real-world code isn't always async-friendly. Legacy libraries, third-party SDKs, file operations — many are synchronous and blocking. Calling them directly inside an async function freezes the event loop:
 
```python
async def bad_example():
    data = requests.get("https://api.example.com")  # BLOCKS the entire event loop
    # No other coroutines can run while this waits!
```
 
### The Solution: `run_in_executor()`
 
`loop.run_in_executor()` runs a blocking function in a thread pool (or process pool) and wraps it as an awaitable — so the event loop stays free while the blocking work runs in the background.
 
### With ThreadPoolExecutor — Blocking I/O
 
Use this when your blocking code does I/O (network, file, DB) and you can't switch to an async library.
 
```python
# 12-04-async-with-thread.py
import asyncio
from concurrent.futures import ThreadPoolExecutor
import requests                              # Synchronous library
 
def check_stock_sync(product_id):            # Regular blocking function
    response = requests.get(f"https://api.example.com/stock/{product_id}")
    return response.json()
 
async def main():
    loop = asyncio.get_event_loop()
 
    with ThreadPoolExecutor(max_workers=4) as executor:
        # run_in_executor runs check_stock_sync in a thread, returns an awaitable
        result = await loop.run_in_executor(
            executor,
            check_stock_sync,
            "product_123"                    # Arguments to the blocking function
        )
    print(f"Stock: {result}")
 
asyncio.run(main())
```
 
The blocking `requests.get()` runs in a thread, freeing the event loop for other coroutines. From async code's perspective, it's just another `await`.
 
### With ProcessPoolExecutor — CPU-Bound Work
 
Use this when the blocking code is CPU-heavy (encryption, compression, ML inference). Threads won't help here due to the GIL — you need separate processes.
 
```python
# 12-05-async-with-process.py
import asyncio
from concurrent.futures import ProcessPoolExecutor
import hashlib
 
def encrypt_data(data: str) -> str:          # CPU-intensive — runs in a separate process
    result = data
    for _ in range(100_000):                 # Simulate heavy computation
        result = hashlib.sha256(result.encode()).hexdigest()
    return result
 
async def main():
    loop = asyncio.get_event_loop()
 
    with ProcessPoolExecutor(max_workers=2) as executor:
        encrypted = await loop.run_in_executor(executor, encrypt_data, "my_secret_data")
    print(f"Encrypted: {encrypted[:20]}...")
 
if __name__ == "__main__":
    asyncio.run(main())
```
 
> **Note:** Always use `if __name__ == "__main__"` with `ProcessPoolExecutor` — same reason as `multiprocessing.Process` (prevents recursive spawning on Windows).
 
### Executor Decision Guide
 
| Blocking Code Type | Executor | Why |
|---|---|---|
| Sync HTTP, file I/O, DB | `ThreadPoolExecutor` | I/O releases GIL; threads fine |
| CPU computation, encryption | `ProcessPoolExecutor` | Bypasses GIL; true parallelism |
| Neither (use async lib) | No executor needed | `aiohttp`, `aiofiles`, `asyncpg` etc. |
 
---
 
## 7. Background Workers and Daemon Threads
 
Sometimes you need work running in the background continuously — logging, health checks, heartbeats — while your main async code runs normally.
 
### Daemon vs Non-Daemon Threads
 
This distinction is critical and often missed.
 
| | Daemon Thread | Non-Daemon Thread |
|---|---|---|
| Exits when main thread exits | ✅ Yes — automatically killed | ❌ No — keeps program alive |
| Use for | Background monitoring, logging | Critical work that must complete |
| Risk | Work may be cut short | Program hangs if thread never finishes |
 
### Example: Background Worker with Daemon Thread
 
```python
# 12-06-bgworker.py
import asyncio
import threading
import time
 
def heartbeat_logger():                      # Runs in background thread
    while True:
        print("[Heartbeat] System alive...")
        time.sleep(2)
 
async def fetch_order(order_id):
    print(f"Fetching order {order_id}...")
    await asyncio.sleep(3)
    print(f"Order {order_id} fetched!")
    return {"id": order_id, "item": "Laptop"}
 
async def main():
    # Start daemon background thread
    monitor = threading.Thread(target=heartbeat_logger, daemon=True)
    monitor.start()                          # Runs independently of async code
 
    # Async work proceeds normally
    order = await fetch_order(42)
    print(f"Result: {order}")
 
asyncio.run(main())
# When main() exits, daemon thread is automatically killed
```
 
### Daemon Thread — Exits with Main
 
```python
# 12-07-daemon.py
import threading
import time
 
def monitor():
    for i in range(100):
        print(f"Monitoring... tick {i}")
        time.sleep(1)
    print("This line never prints")         # Program exits before this
 
t = threading.Thread(target=monitor, daemon=True)
t.start()
 
time.sleep(3)                               # Main thread does 3 seconds of work
print("Main thread done. Daemon dies now.")
# Program exits — daemon thread cut off mid-loop
```
 
### Non-Daemon Thread — Keeps Program Alive
 
```python
# 12-08-non-daemon.py
import threading
import time
 
def monitor():
    while True:
        print("Non-daemon monitoring...")
        time.sleep(1)
 
t = threading.Thread(target=monitor)        # daemon=False by default
t.start()
 
print("Main thread done.")
# ⚠️ Program does NOT exit here — non-daemon thread is still running
# Script hangs forever. Stop with Ctrl+C.
```
 
---
 
## 8. Deadlocks
 
### What is a Deadlock?
 
A **deadlock** occurs when two or more threads are each waiting for a lock held by the other — creating a circular dependency where none can proceed. The program freezes silently.
 
```
Thread A holds Lock 1, waiting for Lock 2
Thread B holds Lock 2, waiting for Lock 1
→ Both wait forever. Nothing moves.
```
 
### Deadlock in Code
 
```python
# 12-09-deadlock.py
import threading
import time
 
lock1 = threading.Lock()
lock2 = threading.Lock()
 
def task_a():
    with lock1:                    # Acquires lock1 first
        print("Task A: got lock1, waiting for lock2...")
        time.sleep(0.1)            # Small delay to ensure task_b acquires lock2
        with lock2:                # Waits for lock2 — but task_b holds it!
            print("Task A: got both locks")
 
def task_b():
    with lock2:                    # Acquires lock2 first — opposite order to task_a
        print("Task B: got lock2, waiting for lock1...")
        time.sleep(0.1)
        with lock1:                # Waits for lock1 — but task_a holds it!
            print("Task B: got both locks")
 
t1 = threading.Thread(target=task_a)
t2 = threading.Thread(target=task_b)
t1.start(); t2.start()
t1.join(); t2.join()               # Hangs here forever — Ctrl+C to stop
```
 
### How to Prevent Deadlocks
 
**Rule: Always acquire locks in the same order everywhere in your code.**
 
```python
# ✅ Both tasks acquire lock1 → lock2 in the same order
def task_a():
    with lock1:
        with lock2:
            print("Task A: done")
 
def task_b():
    with lock1:           # Same order — no circular dependency
        with lock2:
            print("Task B: done")
```
 
Other strategies:
- Use `asyncio` where possible — single-threaded, no lock contention
- Use `threading.RLock()` (reentrant lock) if the same thread needs to acquire the same lock twice
- Use `lock.acquire(timeout=5)` to detect hangs rather than wait forever
---
 
## 9. Profiling Async Code
 
Find where your async code spends time using Python's built-in profiler:
 
```bash
python3 -m cProfile -s time 12-02-run-multiple-routine.py
```
 
`-s time` sorts output by cumulative time — the functions at the top are your bottlenecks.
 
For live profiling of running Python processes (useful for production async servers):
 
```bash
pip install py-spy
py-spy top --pid <your_process_id>
```
 
---
 
## 10. Comparison: asyncio vs threading vs multiprocessing
 
| Scenario | Best Tool | Reason |
|---|---|---|
| Hundreds of concurrent HTTP requests | `asyncio` + `aiohttp` | Single thread, minimal overhead, scales to thousands |
| Legacy sync library you can't replace | `asyncio` + `run_in_executor(ThreadPool)` | Offload blocking I/O to threads without freezing the loop |
| CPU-heavy work (encryption, ML) | `multiprocessing` or `run_in_executor(ProcessPool)` | GIL bypass; true parallel CPU usage |
| Light concurrent I/O, simple code | `threading` | Less overhead to set up than async, good for moderate concurrency |
| Background logging / health checks | Daemon threads | Auto-cleanup; fire and forget |
| High-concurrency web server (FastAPI, etc.) | `asyncio` under the hood | Framework handles the event loop; you just write `async def` |
 
### The Mental Model in One Line
 
- `asyncio` — one chef, switching between dishes every time one needs to wait on the oven
- `threading` — multiple chefs sharing one kitchen, each with their own dish
- `multiprocessing` — multiple chefs in separate kitchens with fully independent setups
---
 
## 11. Common Pitfalls Cheatsheet
 
```python
# ❌ Blocks event loop — never use time.sleep() in async code
async def bad():
    time.sleep(3)
 
# ✅ Use asyncio.sleep() instead
async def good():
    await asyncio.sleep(3)
 
# ❌ requests.get() is synchronous — blocks the loop
async def bad_fetch():
    return requests.get("https://api.example.com")
 
# ✅ Use aiohttp for async HTTP
async def good_fetch(session):
    async with session.get("https://api.example.com") as r:
        return await r.json()
 
# ❌ Calling a coroutine without await — it just creates an object, never runs
async def main():
    brew_coffee()              # Nothing happens! No warning.
 
# ✅ Always await coroutines
async def main():
    await brew_coffee()
 
# ❌ Losing task reference — Python may cancel it
async def main():
    asyncio.create_task(background_work())   # Task may be garbage collected
 
# ✅ Keep a reference
async def main():
    task = asyncio.create_task(background_work())
    await task
 
# ❌ Deadlock — locks acquired in inconsistent order
def thread_a(): lock1 → lock2
def thread_b(): lock2 → lock1   # Opposite order = deadlock
 
# ✅ Always same order
def thread_a(): lock1 → lock2
def thread_b(): lock1 → lock2
```
 
---
 
## Summary
 
| Concept | What it is | Key rule |
|---|---|---|
| `async def` | Coroutine function | Calling it returns an object; must `await` or `asyncio.run()` to execute |
| `await` | Pause + yield control | Only inside `async def`; only works on awaitables |
| Event loop | Scheduler for coroutines | One per thread; started with `asyncio.run()` |
| `gather()` | Run coroutines concurrently | Total time = slowest task, not sum |
| `run_in_executor()` | Bridge sync code into async | ThreadPool for I/O, ProcessPool for CPU |
| Daemon thread | Background thread | Auto-killed when main exits |
| Non-daemon thread | Foreground thread | Keeps program alive until it finishes |
| Deadlock | Circular lock dependency | Prevent by always acquiring locks in the same order |
 
---