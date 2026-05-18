# Multithreading, Multiprocessing & the GIL

## 1. Concurrency vs Parallelism
 
Before diving into code, get these two terms straight — they are often confused.
 
| Term | Meaning | Python Tool |
|---|---|---|
| **Concurrency** | Multiple tasks making progress — not necessarily at the same instant | `threading` |
| **Parallelism** | Multiple tasks literally running at the same instant on separate CPU cores | `multiprocessing` |
 
Think of it this way: a chef juggling multiple dishes is *concurrent* (switching attention). Two chefs cooking separate dishes at the same time is *parallel*.
 
---

## 2. Threading
 
### What is a Thread?
 
A **thread** is the smallest unit of execution within a process. All threads inside a process share the same memory space. This makes them lightweight and fast to create, but also means they need to coordinate carefully when touching shared data.
 
Threads shine for **I/O-bound work** — reading files, making HTTP requests, querying a database — because while one thread waits for a response, others can keep running.

### Core API: `threading.Thread`
 
```python
import threading
 
thread = threading.Thread(target=function_name, args=(arg1, arg2))
thread.start()   # Spawns the thread — starts running target()
thread.join()    # Blocks the caller until this thread finishes
```
 
- `target` — the function the thread will run
- `args` — tuple of arguments passed to the function
- `start()` — actually launches the thread; calling it is non-blocking (your main code continues immediately)
- `join()` — wait here until the thread is done; without this, your main program can exit before threads finish
### Example 1 — Basic Threading (Restaurant Kitchen)
 
```python
# 11-01-threading.py
import threading
import time
 
def take_order(order_id):
    print(f"Taking order {order_id}...")
    time.sleep(1)                            # Simulate waiter walking to table
    print(f"Order {order_id} taken!")
 
def cook_order(order_id):
    print(f"Cooking order {order_id}...")
    time.sleep(2)                            # Simulate cooking time
    print(f"Order {order_id} ready!")
 
# Create threads — they don't start yet
t1 = threading.Thread(target=take_order, args=(1,))
t2 = threading.Thread(target=cook_order, args=(1,))
 
t1.start()   # Both threads start — they run concurrently
t2.start()
 
t1.join()    # Main thread waits for t1 to finish
t2.join()    # Main thread waits for t2 to finish
 
print("Service complete.")
```

**What's happening:**  
Both `take_order` and `cook_order` run concurrently. Without threading, you'd wait 1s + 2s = 3s total. With threading, both overlap and complete in ~2s.

### Example 2 — I/O-Bound: Downloading Images
 
This is where threading genuinely helps. The `requests` library releases the GIL while waiting for a network response, so multiple threads can overlap their waiting time.
 
```python
# 11-05-threading-detail.py
import threading
import requests
import time
 
IMAGE_URLS = [
    "https://picsum.photos/id/1/200",
    "https://picsum.photos/id/2/200",
    "https://picsum.photos/id/3/200",
    "https://picsum.photos/id/4/200",
]
 
def download_image(url):
    response = requests.get(url)            # GIL is released here while waiting
    print(f"Downloaded {len(response.content)} bytes from {url}")
 
start = time.time()
 
threads = []
for url in IMAGE_URLS:
    t = threading.Thread(target=download_image, args=(url,))
    threads.append(t)
    t.start()                               # All downloads start almost simultaneously
 
[t.join() for t in threads]                               # Wait for all downloads to complete
 
print(f"All downloads done in {time.time() - start:.2f}s")
```
 
**Without threading:** downloads happen sequentially — total time = sum of all download times.  
**With threading:** downloads overlap — total time ≈ slowest single download.
 
> **Setup note:** This example needs the `requests` library. Use a virtual environment:
> ```bash
> python3 -m venv venv
> source venv/bin/activate   # Windows: venv\Scripts\activate
> pip install requests
> python3 11-05-threading-detail.py
> ```

---
 
## 3. Multiprocessing
 
### What is a Process?
 
A **process** is a completely independent program in execution, with its own memory space, its own Python interpreter, and its own GIL. Because processes don't share memory, they can truly run in parallel across multiple CPU cores.
 
This makes multiprocessing ideal for **CPU-bound work** — heavy computation, image processing, data crunching — where you actually need multiple cores doing work simultaneously.
 
The trade-off: processes are heavier to create than threads, and sharing data between them requires explicit IPC (inter-process communication) mechanisms like `Queue` and `Value`.
 
### Core API: `multiprocessing.Process`
 
```python
from multiprocessing import Process
 
p = Process(target=function_name, args=(arg1,))
p.start()   # Spawns a new OS process
p.join()    # Wait for it to finish
```
 
The API mirrors `threading.Thread` deliberately — same `target`, `args`, `start()`, `join()` pattern.
 
### The `if __name__ == "__main__"` Guard
 
On Windows (and for safe cross-platform code), always wrap your process-spawning code in this guard:
 
```python
if __name__ == "__main__":
    p = Process(target=my_func)
    p.start()
    p.join()
```
 
Without it, Windows can infinitely recurse — spawning processes that spawn more processes. On macOS/Linux this matters less but is still good practice.
 
### Example 3 — Basic Multiprocessing
 
```python
# 11-02-multiprocessing.py
from multiprocessing import Process
import time
 
def cook(chef_name, dish):
    print(f"{chef_name} starts cooking {dish}...")
    time.sleep(2)                            # Simulates CPU work
    print(f"{chef_name} finished cooking {dish}!")
 
if __name__ == "__main__":
    p1 = Process(target=cook, args=("Chef A", "Biryani"))
    p2 = Process(target=cook, args=("Chef B", "Dal Makhani"))
 
    p1.start()                               # Two truly parallel processes
    p2.start()
 
    p1.join()
    p2.join()
 
    print("Both dishes ready!")
```
 
### Example 4 — CPU-Bound: Sum of Large Numbers
 
```python
# 11-07-multiprocessing-detail.py
from multiprocessing import Process
import time
 
def compute_sum(n):
    total = sum(range(n))
    print(f"Sum up to {n}: {total}")
 
if __name__ == "__main__":
    N = 50_000_000
 
    # Sequential baseline
    start = time.time()
    compute_sum(N)
    compute_sum(N)
    print(f"Sequential: {time.time() - start:.2f}s")
 
    # Parallel with multiprocessing
    start = time.time()
    p1 = Process(target=compute_sum, args=(N,))
    p2 = Process(target=compute_sum, args=(N,))
    p1.start(); p2.start()
    p1.join(); p2.join()
    print(f"Parallel: {time.time() - start:.2f}s")
```
 
On a multi-core machine, the parallel version runs ~2x faster for this CPU-bound task — something threading *cannot* achieve due to the GIL.
 
---
 
## 4. The Global Interpreter Lock (GIL)
 
### What is the GIL?
 
The **Global Interpreter Lock** is a mutex (mutual exclusion lock) built into CPython (the standard Python interpreter). It ensures that **only one thread executes Python bytecode at any given moment**, even on a multi-core CPU.
 
### Why Does It Exist?
 
CPython's memory management (reference counting for garbage collection) is not thread-safe. The GIL protects Python's internal state — object reference counts, memory allocations — from race conditions without requiring fine-grained locks on every object.
 
### The Race Condition Problem It Solves
 
Imagine two threads both doing `x += 1` where `x = 0`. Internally this is:
1. Read `x` → 0
2. Add 1 → 1
3. Write back → `x = 1`
If two threads interleave at step 2, both read `0`, both compute `1`, and both write `1`. You expected `x = 2`, you got `x = 1`. That's a race condition. The GIL prevents this at the interpreter level.
 
### GIL in Action: Threading vs Multiprocessing on CPU-Bound Work
 
```python
# 11-03-gil-threading.py — GIL LIMITS THIS
import threading
import time
 
def count_up(n):
    total = 0
    for _ in range(n):
        total += 1
    return total
 
N = 50_000_000
start = time.time()
 
t1 = threading.Thread(target=count_up, args=(N,))
t2 = threading.Thread(target=count_up, args=(N,))
 
t1.start(); t2.start()
t1.join(); t2.join()
 
print(f"Threading (CPU-bound): {time.time() - start:.2f}s")
# ❌ This will NOT be faster than single-threaded. Both threads fight over the GIL.
```
 
```python
# 11-04-gil-multiprocessing.py — GIL DOES NOT APPLY
from multiprocessing import Process
import time
 
def count_up(n):
    total = 0
    for _ in range(n):
        total += 1
    return total
 
if __name__ == "__main__":
    N = 50_000_000
    start = time.time()
 
    p1 = Process(target=count_up, args=(N,))
    p2 = Process(target=count_up, args=(N,))
 
    p1.start(); p2.start()
    p1.join(); p2.join()
 
    print(f"Multiprocessing (CPU-bound): {time.time() - start:.2f}s")
    # ✅ Each process has its own GIL — true parallelism, ~2x faster on dual-core
```
 
**Expected results on a 4-core machine:**
 
| Approach | CPU-Bound Time | Notes |
|---|---|---|
| Single-threaded | ~5s | Baseline |
| `threading` | ~5-6s | Same or *slower* (GIL contention overhead) |
| `multiprocessing` | ~2-3s | Genuinely faster — each process has its own GIL |
 
### GIL and I/O-Bound Work
 
Here's the important nuance: **the GIL is released during I/O operations.**
 
When a thread is waiting for a network response, disk read, or database query — it's not executing Python bytecode. During that wait, it voluntarily releases the GIL, letting other threads run. This is why `threading` still works well for I/O-bound tasks.
 
```
CPU-bound:  Thread A ██████████ Thread B ██████████  (serialized — GIL held)
I/O-bound:  Thread A █░░░░░░░░█ Thread B   █░░░░░░░░█  (overlap during wait)
                      ↑ waiting (GIL released)
```
 
---
 
## 5. Thread Synchronization — `Lock`
 
### The Race Condition Problem
 
Even with the GIL, race conditions can happen in multi-step operations. Consider incrementing a shared counter from multiple threads:
 
```python
# Without a Lock — BROKEN
import threading
 
counter = 0
 
def increment():
    global counter
    for _ in range(100_000):
        counter += 1           # Read-modify-write: NOT atomic even with GIL
 
threads = [threading.Thread(target=increment) for _ in range(5)]
for t in threads: t.start()
for t in threads: t.join()
 
print(counter)                 # Expected: 500,000 — Actual: something less, unpredictably
```
 
The GIL doesn't make `counter += 1` atomic. The GIL can switch threads between the read and the write.
 
### Using `threading.Lock()`
 
```python
# 11-06-thread-lock.py — CORRECT
import threading
 
counter = 0
lock = threading.Lock()        # One lock shared by all threads
 
def increment():
    global counter
    for _ in range(100_000):
        with lock:             # Only one thread can be inside this block at a time
            counter += 1       # Safe: read-modify-write is now protected
 
threads = [threading.Thread(target=increment) for _ in range(5)]
for t in threads: t.start()
for t in threads: t.join()
 
print(counter)                 # Always 500,000 ✅
```
 
### How `Lock` Works
 
```
Thread A: acquire() → [LOCKED] → do work → release()
Thread B: acquire() → BLOCKED (waiting) → ... → [LOCKED] → do work → release()
Thread C: acquire() → BLOCKED (waiting) → ...
```
 
- `lock.acquire()` — claim the lock; if already held, block until it's released
- `lock.release()` — release the lock; the next waiting thread can acquire it
- `with lock:` — the Pythonic way; automatically acquires on entry, releases on exit (even if an exception occurs)
> **Rule of thumb:** Use a `Lock` any time multiple threads read *and write* the same shared variable.
 
---
 
## 6. Inter-Process Communication — `Queue` & `Value`
 
Since processes have separate memory spaces, they can't share variables directly. Python's `multiprocessing` module provides two main tools:
 
### `multiprocessing.Value` — Shared Primitive
 
`Value` creates a C-type variable in shared memory that multiple processes can access.
 
```python
# Part of 11-08-processing-queue.py
from multiprocessing import Process, Value
import ctypes
 
def add_to_total(shared_val, amount):
    with shared_val.get_lock():            # Lock is built in — always use it!
        shared_val.value += amount
 
if __name__ == "__main__":
    total = Value(ctypes.c_int, 0)         # Shared integer, initialized to 0
 
    processes = [
        Process(target=add_to_total, args=(total, 100))
        for _ in range(5)
    ]
    for p in processes: p.start()
    for p in processes: p.join()
 
    print(f"Total: {total.value}")         # 500 ✅
```
 
Key points:
- `Value('i', 0)` or `Value(ctypes.c_int, 0)` — 'i' is shorthand for integer
- `.value` — access or modify the underlying data
- `.get_lock()` — returns the built-in lock; always use it to avoid race conditions across processes
### `multiprocessing.Queue` — Message Passing
 
`Queue` is a thread- and process-safe FIFO queue for sending data between processes.
 
```python
# 11-08-processing-queue.py
from multiprocessing import Process, Queue
 
def producer(queue, items):
    for item in items:
        print(f"Producing: {item}")
        queue.put(item)                    # Send data into the queue
    queue.put(None)                        # Sentinel: signals "no more items"
 
def consumer(queue):
    while True:
        item = queue.get()                 # Receive data; blocks until something arrives
        if item is None:
            break                          # Sentinel received — stop
        print(f"Consuming: {item}")
 
if __name__ == "__main__":
    q = Queue()
 
    p1 = Process(target=producer, args=(q, [1, 2, 3, 4, 5]))
    p2 = Process(target=consumer, args=(q,))
 
    p1.start(); p2.start()
    p1.join(); p2.join()
```
 
**`Queue` vs `Value`:**
 
| | `Value` | `Queue` |
|---|---|---|
| Use for | Single shared number/flag | Passing multiple items between processes |
| Direction | Read/write by any process | Producer → Consumer |
| Blocking | No (use lock manually) | `get()` blocks until item available |
 
---
 
## 7. When to Use What
 
| Task Type | Examples | Best Tool | Why |
|---|---|---|---|
| I/O-bound | HTTP requests, file reads, DB queries | `threading` | GIL released during I/O; threads cheap to create |
| CPU-bound | Image processing, ML inference, data crunching | `multiprocessing` | Bypasses GIL; true parallelism across cores |
| Single-threaded async I/O | High-concurrency web servers | `asyncio` | Even lower overhead than threads for I/O |
| Mixed workload | Worker pool + I/O per worker | Both | `multiprocessing.Pool` + threads inside each worker |
 
### Decision Flowchart
 
```
Is your bottleneck waiting for something external (network, disk)?
  └─ YES → threading (or asyncio for very high concurrency)
  └─ NO (pure computation) → multiprocessing
 
Need to share simple data between processes?
  └─ Single value/flag → multiprocessing.Value
  └─ Stream of items → multiprocessing.Queue
 
Need to protect shared state in threads?
  └─ threading.Lock
```
 
---
 
## 8. Quick Reference Cheatsheet
 
```python
# ── THREADING ──────────────────────────────────────────────────
import threading
 
t = threading.Thread(target=fn, args=(a,))
t.start()           # Launch thread (non-blocking)
t.join()            # Wait for thread to finish
 
lock = threading.Lock()
with lock:          # Protect critical section
    shared_data += 1
 
 
# ── MULTIPROCESSING ────────────────────────────────────────────
from multiprocessing import Process, Queue, Value
import ctypes
 
p = Process(target=fn, args=(a,))
p.start()
p.join()
 
q = Queue()
q.put(item)         # Send (from producer)
item = q.get()      # Receive, blocks until available (in consumer)
 
v = Value(ctypes.c_int, 0)
with v.get_lock():
    v.value += 1
 
 
# ── GUARDS ─────────────────────────────────────────────────────
if __name__ == "__main__":   # Always wrap multiprocessing entry point
    p = Process(target=fn)
    p.start()
    p.join()
```
 
---
 
## Summary
 
- **Threads** share memory, are lightweight, and help with I/O-bound tasks. The GIL limits their usefulness for CPU-bound work.
- **Processes** have separate memory, bypass the GIL, and provide true CPU parallelism — at the cost of higher creation overhead and explicit IPC.
- **The GIL** is CPython's internal lock that allows only one thread to execute Python bytecode at a time. It is released during I/O, which is why threading still helps for network/disk work.
- Use **`Lock`** to protect shared mutable state across threads.
- Use **`Value`** and **`Queue`** to share data safely across processes.
---
    