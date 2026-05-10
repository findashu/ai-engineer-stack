# Python Generators and Decorators

This module covers Python generators and decorators with practical examples. You will learn how generators produce values lazily, how to consume them with `next()` and `send()`, how to use `yield from` for delegation, and how decorators wrap functions to add behavior.

---

## Table of Contents

1. [Generators](#1-generators)
   - [What is a Generator?](#what-is-a-generator)
   - [How Generators Work Internally](#how-generators-work-internally)
   - [Why Use Generators?](#why-use-generators)
   - [The `yield` Keyword](#the-yield-keyword)
   - [The `next()` Function](#the-next-function)
   - [The `send()` Method](#the-send-method)
   - [The `yield from` Statement](#the-yield-from-statement)
   - [Closing a Generator](#closing-a-generator)
   - [When NOT to Use Generators](#when-not-to-use-generators)
2. [Decorators](#2-decorators)
   - [What is a Decorator?](#what-is-a-decorator)
   - [How Decorators Work Internally](#how-decorators-work-internally)
   - [The `@` Syntax](#the--syntax)
   - [Preserving Metadata with `functools.wraps`](#preserving-metadata-with-functoolswraps)
   - [Real-World Use Cases](#real-world-use-cases)
3. [Concept Comparison Table](#3-concept-comparison-table)
4. [Common Pitfalls](#4-common-pitfalls)
5. [Takeaways](#5-takeaways)

---

## 1. Generators

A **generator** is a special type of function that does not run to completion in one shot. Instead, it **pauses at each `yield` statement** and resumes from the same point when called again.

Think of a generator like a **bookmark in a book** — you read a few pages, put the bookmark in, close the book, and when you open it again, you continue from exactly where you left off. The rest of the book is not loaded into your memory all at once.

Generators return a **generator object** when called. This object is an **iterator** — meaning you can loop over it or manually step through it.

```
Regular function:  called → runs fully → returns one value → done
Generator:         called → returns generator object
                   next() → runs until yield → pauses → remembers state
                   next() → resumes → runs until next yield → pauses again
                   next() → no more yields → raises StopIteration
```

### How Generators Work Internally

When Python encounters a function with a `yield` keyword, it does **not execute it** — it compiles it into a generator function. Calling that function returns a generator object without running any code inside.

The generator object maintains:
- Its **local variables** and their current values
- Its **current position** in the code (which `yield` it paused at)
- Its **execution stack frame**

This is what makes generators stateful — they remember where they were.

```python
def my_gen():
    print("Step 1")
    yield 10
    print("Step 2")
    yield 20

g = my_gen()     # Nothing runs yet — only a generator object is created
next(g)          # Runs until first yield → prints "Step 1" → returns 10
next(g)          # Resumes → prints "Step 2" → returns 20
next(g)          # Nothing left → raises StopIteration
```

---

### Why Use Generators?

Generators shine in scenarios where you need to work with **large or potentially infinite sequences** without storing them all in memory.

| Without Generator | With Generator |
|---|---|
| Build full list in memory | Produce one value at a time |
| `[x for x in range(1_000_000)]` loads all 1M items | `(x for x in range(1_000_000))` loads nothing upfront |
| Random access is possible | Only sequential access |
| Faster for repeated access | Faster for one-pass access |

**Generators are ideal for:**
- Reading large files line by line
- Infinite streams (e.g., sensor data, live feeds)
- Data pipelines and processing chains
- Lazy evaluation of expensive computations

---

### The `yield` Keyword

`yield` is the heart of a generator. It has two roles:

1. **Producer role** — it sends a value out to the caller
2. **Consumer role** — it can receive a value back via `send()`

When Python hits `yield`, it:
1. Returns the yielded value to whoever called `next()`
2. **Suspends** the function at that exact line
3. Saves all local variables and the execution position

```python
def counter():
    n = 0
    while True:
        yield n     # pauses here, sends n out
        n += 1      # resumes here on next call
```

> [!NOTE]
> A function with even a single `yield` anywhere in its body becomes a generator function, regardless of whether that `yield` is always reached.

---

### The `next()` Function

`next()` is how you **advance a generator** by one step. It resumes the generator from its paused position and runs it until the next `yield`.

**Behaviour summary:**

| Situation | Result |
|---|---|
| Generator not yet started | Runs from the beginning to the first `yield` |
| Generator paused at a `yield` | Resumes from that point to the next `yield` |
| Generator already exhausted | Raises `StopIteration` |

```python
gen = my_generator()

next(gen)   # first yield
next(gen)   # second yield
next(gen)   # StopIteration raised
```

You can also provide a **default value** to avoid `StopIteration`:

```python
value = next(gen, "no more values")
```

**When to use `next()` directly:**
- When you need to consume just one value at a time
- When you want fine-grained control over iteration
- When building custom iterators or state machines

---

### The `send()` Method

`send()` is a more powerful form of `next()`. While `next()` only resumes the generator, `send(value)` **resumes it AND injects a value** back into the generator — making the current `yield` expression evaluate to that value.

This enables **two-way communication** between the caller and the generator.

**Key rules:**
- The generator must be **primed** (started) first using `next()` or `send(None)` before you can send an actual value
- The value passed to `send()` becomes the result of the `yield` expression inside the generator
- `send()` still returns the next yielded value, just like `next()`

```
Caller                         Generator
------                         ---------
next(gen)          →           starts, runs to yield
                   ←           yields value A (paused)
gen.send("hello")  →           resumes, "hello" becomes the yield result
                   ←           yields value B (paused again)
```

**Typical use cases for `send()`:**
- Coroutine-style patterns (producer/consumer pipelines)
- Interactive generators that react to external input
- Stateful computation loops where the next step depends on external feedback

> [!IMPORTANT]
> Calling `send(value)` on an unstarted generator raises `TypeError`. Always prime it first with `next()` or `send(None)`.

---

### The `yield from` Statement

`yield from` is syntactic sugar introduced in Python 3.3 to **delegate iteration to a sub-generator**. Instead of manually looping and re-yielding values from an inner generator, `yield from` does it automatically and more efficiently.

**Without `yield from`:**
```python
def outer():
    for value in inner_generator():
        yield value    # tedious manual delegation
```

**With `yield from`:**
```python
def outer():
    yield from inner_generator()   # clean and direct
```

Beyond simplicity, `yield from` also:
- Properly **forwards `send()` calls** into the sub-generator
- Propagates **exceptions** correctly through the chain
- Returns the sub-generator's **final return value** to the delegating generator

This makes `yield from` essential for building **generator pipelines** and **coroutine chains**.

---

### Closing a Generator

Every generator object has a `.close()` method. Calling it throws a `GeneratorExit` exception inside the generator at the point where it is paused, allowing it to clean up resources.

```python
gen = my_generator()
next(gen)
gen.close()   # GeneratorExit is thrown into the generator
```

You can handle this gracefully inside the generator:

```python
def my_gen():
    try:
        yield 1
        yield 2
    finally:
        print("Generator closed — cleaning up")
```

> [!NOTE]
> If a generator is garbage collected without being explicitly closed, Python calls `.close()` automatically.

---

### When NOT to Use Generators

Generators are not always the right tool. Avoid them when:

- You need **random access** (e.g., `items[5]`) — generators are forward-only
- You need to **iterate multiple times** — a generator is exhausted after one pass; you'd need to rebuild it
- The sequence is **small and cheap** to build — a list is simpler and faster for small data
- You need `len()` — generators have no concept of length

---

## 2. Decorators

### What is a Decorator?

A **decorator** is a design pattern in Python that allows you to **wrap a function with additional behaviour** without modifying its original source code. Decorators follow the **Open/Closed Principle** — open for extension, closed for modification.

In practical terms, a decorator is a **callable that takes a function and returns a new function** that adds something before and/or after the original function runs.

```
Original function:   does its job

Decorated function:  → runs extra code before
                     → calls the original function
                     → runs extra code after
                     → returns result
```

---

### How Decorators Work Internally

A decorator is essentially a **higher-order function** — a function that accepts another function as an argument and returns a new, enhanced function.

```python
def my_decorator(func):          # takes a function
    def wrapper(*args, **kwargs):
        # code before
        result = func(*args, **kwargs)   # calls original
        # code after
        return result
    return wrapper               # returns a new function
```

When you decorate a function, Python replaces the original function reference with the wrapper:

```python
def greet():
    print("Hello!")

greet = my_decorator(greet)   # greet now points to wrapper
greet()                       # actually calls wrapper, which calls original greet
```

The `@` syntax is just shorthand for the above reassignment.

---

### The `@` Syntax

The `@decorator` syntax placed above a function definition is **exactly equivalent** to calling the decorator and reassigning:

```python
# These two are identical:

@my_decorator
def greet():
    print("Hello!")

# is the same as:

def greet():
    print("Hello!")
greet = my_decorator(greet)
```

You can also **stack multiple decorators**. They are applied bottom-up:

```python
@decorator_a
@decorator_b
def my_function():
    pass

# Equivalent to:
my_function = decorator_a(decorator_b(my_function))
```

---

### Preserving Metadata with `functools.wraps`

A common problem with decorators is that the wrapper function **replaces the original's identity**. After decoration, `function.__name__`, `function.__doc__`, and other metadata point to the wrapper instead of the original.

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet():
    """Says hello."""
    print("Hello!")

print(greet.__name__)   # prints "wrapper" — wrong!
print(greet.__doc__)    # prints None — wrong!
```

**`functools.wraps`** fixes this by copying the original function's metadata onto the wrapper:

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)              # copies __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet():
    """Says hello."""
    print("Hello!")

print(greet.__name__)   # prints "greet" — correct!
print(greet.__doc__)    # prints "Says hello." — correct!
```

> [!IMPORTANT]
> Always use `@wraps(func)` inside your decorators. It is essential for debugging, introspection, documentation tools, and frameworks that rely on function names.

---

### Real-World Use Cases

Decorators are used extensively in Python codebases and frameworks:

| Use Case | What the Decorator Does |
|---|---|
| **Logging** | Prints function name, arguments, and return value automatically |
| **Timing** | Measures and reports how long a function takes to run |
| **Authorization** | Checks user role or permission before allowing execution |
| **Caching / Memoization** | Stores results of expensive calls and returns cached results for same inputs |
| **Retry Logic** | Automatically retries a function if it raises an exception |
| **Rate Limiting** | Prevents a function from being called too frequently |
| **Validation** | Checks argument types or values before the function runs |

Python's standard library includes ready-made decorators: `@staticmethod`, `@classmethod`, `@property`, and `@functools.lru_cache` (memoization).

Frameworks like Flask and Django use decorators extensively:
```python
@app.route("/home")       # Flask — registers a URL route
@login_required           # Django — enforces authentication
```

---

## 3. Concept Comparison Table

| Concept | Purpose | Key Syntax | Returns |
|---|---|---|---|
| `yield` | Pause and produce a value | `yield value` | Sends value to caller |
| `next()` | Advance the generator one step | `next(gen)` | Next yielded value |
| `send()` | Advance and inject a value | `gen.send(val)` | Next yielded value |
| `yield from` | Delegate to a sub-generator | `yield from gen` | Sub-generator's return value |
| `.close()` | Terminate a generator | `gen.close()` | None |
| Decorator | Wrap a function with extra behaviour | `@decorator` | New wrapped function |
| `@wraps` | Preserve original function metadata | `@wraps(func)` | Wrapper with copied metadata |

---

## 4. Common Pitfalls

> [!CAUTION]
> **Generator exhaustion** — Once a generator is fully consumed, it is empty. Calling `next()` again raises `StopIteration`. You must recreate it to iterate again.

> [!CAUTION]
> **Unprimed generator + `send()`** — Calling `send(value)` before `next()` on a fresh generator raises `TypeError`. Always prime with `next()` or `send(None)` first.

> [!WARNING]
> **Missing `@wraps`** — Forgetting `functools.wraps` in your decorator breaks introspection tools, test frameworks, and documentation generators that rely on `__name__` and `__doc__`.

> [!WARNING]
> **Stacking decorators in wrong order** — Decorators apply bottom-up. The order matters especially when combining authentication and logging decorators.

> [!NOTE]
> **Generator vs Generator Expression** — `(x for x in range(10))` is a generator expression (one-liner, no `yield`). A generator function uses `def` + `yield` and can hold complex logic with multiple yields.

---

## 5. Takeaways

- **Generators are lazy** — they produce values on demand, making them memory-efficient for large or infinite sequences.
- **`yield` pauses execution** and remembers state; the generator resumes from the exact same point on the next call.
- **`next()`** advances the generator one step; **`send()`** does the same but also injects a value back in, enabling two-way communication.
- **`yield from`** delegates iteration to a sub-generator cleanly, and also properly forwards `send()` calls and exceptions.
- **Decorators wrap functions** to add reusable behaviour (logging, auth, caching) without modifying the original function.
- **`functools.wraps`** is not optional — always include it to preserve the original function's identity and metadata.
- Both generators and decorators are examples of Python embracing **composability and separation of concerns**.
