# Exception Handling & File I/O

Errors are not failures — they're information. Python's exception system lets you handle the unexpected gracefully, keep resources safe, and give users meaningful feedback instead of a crash.
 
---
 
## Quick Reference
 
| Keyword | Purpose |
|---|---|
| `try` | Wrap code that might fail |
| `except` | Handle a specific exception |
| `else` | Runs only if `try` succeeded (no exception) |
| `finally` | Always runs — cleanup, logging, closing connections |
| `raise` | Manually throw an exception |
| `Exception` | Base class for all built-in exceptions |
| `with` | Context manager — auto-cleanup on exit |
 
---

## 1. How Python Handles Errors
 
When Python hits an error it can't handle, it raises an **exception** — an object that describes what went wrong. If nothing catches it, the program crashes with a **traceback**.
 
```
Traceback (most recent call last):
  File "app.py", line 3, in <module>
    employee["lastname"]
KeyError: 'lastname'
```
 
Read a traceback **bottom-up** — the last line tells you the exception type and message. The lines above show the call stack leading to it.

 
### Common built-in exceptions
 
| Exception | When it occurs |
|---|---|
| `IndexError` | List index out of range |
| `KeyError` | Dictionary key doesn't exist |
| `TypeError` | Wrong type passed to an operation |
| `ValueError` | Right type, but invalid value (e.g. `int("abc")`) |
| `NameError` | Variable used before being defined |
| `FileNotFoundError` | File doesn't exist at the given path |
| `ZeroDivisionError` | Division by zero |
| `AttributeError` | Attribute doesn't exist on an object |
 
📄 `10-01-error.py`
 
---

 
## 2. `try` / `except`
 
Wrap risky code in `try`. If an exception is raised, Python immediately jumps to the matching `except` block — the rest of `try` is skipped.
 
```python
employee = {"name": "John", "age": 30}
 
try:
    print(employee["lastname"])   # raises KeyError
except KeyError:
    print("Last name not found")
 
print("Program continues")       # this still runs
```
 
**Without the `try/except`**, the program would crash at `employee["lastname"]` and `"Program continues"` would never print.
 
> Always catch the **most specific** exception you expect. Catching a broad `Exception` everywhere hides bugs.
 
📄 `10-02-try-except.py`
 
---

## 3. `try` / `except` / `else` / `finally`
 
The full exception handling structure gives you fine-grained control over success, failure, and cleanup paths.
 
```python
def serve_coffee(flavour):
    try:
        if flavour == "unknown":
            raise ValueError("We don't have that flavour.")
        print(f"Preparing {flavour} coffee...")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"Here is your {flavour} coffee!")   # only if no exception
    finally:
        print("Next customer please")              # always runs
 
serve_coffee("latte")
# Preparing latte coffee...
# Here is your latte coffee!
# Next customer please
 
serve_coffee("unknown")
# Error: We don't have that flavour.
# Next customer please
```

### How each block is used
 
```
try:      → the code you want to run
except:   → what to do when it fails
else:     → what to do when it succeeds (keeps success path clean)
finally:  → cleanup that must happen no matter what
           (closing DB connections, releasing locks, logging)
```
 
> `else` exists to separate "success logic" from "attempt logic". Without it, you'd put success code inside `try`, where a new exception could accidentally get caught by your `except`.
 
📄 `10-03-try-except-else-finally.py`

---

## 4. Catching Multiple Exceptions
 
Different failures need different responses. Add multiple `except` blocks — Python checks them top to bottom and runs the first match.
 
```python
def process_order(item, quantity):
    try:
        price = {"latte": 3.50, "cappuccino": 4.00, "espresso": 3.00}[item]
        cost = price * quantity
        print(f"Total cost: ${cost:.2f}")
    except KeyError:
        print("Sorry, that coffee is not on the menu")
    except TypeError:
        print("Quantity must be a number")
```
 
```python
process_order("latte", 2)        # Total cost: $7.00
process_order("mocha", 2)        # Sorry, that coffee is not on the menu
process_order("latte", "two")    # Quantity must be a number
```
 
### Catching multiple in one line
 
```python
except (KeyError, TypeError) as e:
    print(f"Order failed: {e}")
```
 
Use this when different exceptions need the same response.
 
> **Order matters.** Put more specific exceptions before broader ones. If `except Exception` comes first, it swallows everything below it.
 
📄 `10-04-catching-multiple-exception.py`
 
---
 
## 5. Custom Exceptions
 
Built-in exceptions are generic. Custom exceptions make your error handling **self-documenting** — the exception name itself tells you exactly what went wrong.
 
```python
# Using a generic ValueError — works, but vague
def brew(flavour):
    if flavour not in ["masala", "ginger", "cardamom"]:
        raise ValueError("Invalid flavour.")
 
 
# Using a custom exception — clear and specific
class InvalidFlavourError(Exception):
    pass
 
 
def brew(flavour):
    if flavour not in ["masala", "ginger", "cardamom"]:
        raise InvalidFlavourError(f"'{flavour}' is not available. Choose: masala, ginger, cardamom.")
    print(f"Brewing {flavour} tea.")
 
 
try:
    brew("lemon")
except InvalidFlavourError as e:
    print(f"Flavour error: {e}")
```
 
### Why `class InvalidFlavourError(Exception): pass` works
 
- Inheriting from `Exception` gives your class all exception behaviour (message, traceback, etc.)
- `pass` means no custom logic needed — the name alone carries the meaning
- Callers can catch `InvalidFlavourError` specifically without catching unrelated `ValueError`s
### Adding more context to custom exceptions
 
```python
class InvalidFlavourError(Exception):
    def __init__(self, flavour, available):
        self.flavour = flavour
        super().__init__(f"'{flavour}' not available. Choose from: {', '.join(available)}")
 
raise InvalidFlavourError("lemon", ["masala", "ginger", "cardamom"])
# InvalidFlavourError: 'lemon' not available. Choose from: masala, ginger, cardamom
```
 
📄 `10-05-custom-exception.py`
 
---
 
## 6. Mini Project — Billing with Validation
 
Combines everything: custom exception, type checking, multiple failure paths, and a single catch point.
 
```python
class InvalidCoffeeError(Exception):
    pass
 
 
def bill(flavour, cups):
    menu = {"latte": 20, "espresso": 30, "cappuccino": 40}
    try:
        if flavour not in menu:
            raise InvalidCoffeeError(f"'{flavour}' is not on the menu.")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an integer.")
        total = menu[flavour] * cups
        print(f"Total bill for {cups} {flavour}(s): ₹{total}")
    except Exception as e:
        print(f"Billing error: {e}")
 
 
bill("latte", 3)        # Total bill for 3 latte(s): ₹60
bill("latte", "3")      # Billing error: Number of cups must be an integer.
bill("unknown", 3)      # Billing error: 'unknown' is not on the menu.
```
 
> `except Exception as e` at the end of a chain is fine as a **last resort catch-all** — but don't use it as a first line of defence. It masks bugs if overused.
 
📄 `10-06-mini-project.py`
 
---
 
## 7. File Handling
 
Files are external resources — if your code crashes mid-operation without closing a file, you can corrupt data or leak file handles. The `with` statement solves this automatically.
 
### File modes
 
| Mode | Meaning |
|---|---|
| `"r"` | Read (default) — file must exist |
| `"w"` | Write — creates file, **overwrites** if exists |
| `"a"` | Append — adds to end, creates if not exists |
| `"r+"` | Read + write |
| `"rb"` / `"wb"` | Binary mode (images, PDFs, etc.) |
 
### Writing a file
 
```python
with open("notes.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Second line.\n")
```
 
`with` calls `file.close()` automatically when the block exits — even if an exception occurs. You never need to call `.close()` manually.
 
### Reading a file
 
```python
# Read entire file as a string
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
 
# Read line by line (memory efficient for large files)
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())
 
# Read all lines into a list
with open("notes.txt", "r") as file:
    lines = file.readlines()   # ['Hello, World!\n', 'Second line.\n']
```
 
### Appending to a file
 
```python
with open("notes.txt", "a") as file:
    file.write("This is added without overwriting.\n")
```
 
### Handling missing files
 
```python
try:
    with open("missing.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found — check the path.")
```
 
> 💡 **Senior tip:** For production file handling, use `pathlib.Path` instead of raw strings — it's cleaner, cross-platform, and avoids path separator bugs:
> ```python
> from pathlib import Path
>
> path = Path("data") / "notes.txt"    # works on Windows and macOS
>
> if path.exists():
>     content = path.read_text()       # no open() needed for simple reads
>
> path.write_text("Hello, World!")     # no open() needed for simple writes
> ```
 
📄 `10-07-file-handling.py`
 
---
 
## Engineer Tips
 
> 💡 **Be specific with exceptions.** `except Exception` everywhere is the exception handling equivalent of `SELECT *` — you get everything, including things you didn't want.
 
> 💡 **Never silently swallow exceptions.** This is a common mistake:
> ```python
> try:
>     do_something()
> except Exception:
>     pass    # ← bug disappears here, never to be found again
> ```
> At minimum, log it: `logging.exception("Something failed")`
 
> 💡 **`raise` without arguments re-raises the current exception.** Useful when you want to log and re-raise:
> ```python
> try:
>     process()
> except ValueError as e:
>     logging.error(f"Validation failed: {e}")
>     raise    # re-raises the same ValueError up the call stack
> ```
 
> 💡 **Build a custom exception hierarchy for larger projects.** Group related errors under a base class so callers can choose how specific to be:
> ```python
> class AppError(Exception): pass          # catch-all for your app
> class DatabaseError(AppError): pass      # DB-specific
> class ValidationError(AppError): pass    # input validation
>
> # Caller can catch broadly or specifically
> except AppError: ...          # catches all of the above
> except ValidationError: ...   # catches only validation issues
> ```
 
> 💡 **This module is the foundation for AI/API work.** Every external API call — OpenAI, Hugging Face, vector stores — will throw exceptions on bad input, rate limits, or network failures. The patterns here (try/except, custom exceptions, finally for cleanup) apply directly.
 
---
 
## Key Takeaways
 
- Exceptions are objects — they carry type, message, and traceback.
- `try/except` catches failures; `else` handles success; `finally` always cleans up.
- Catch the most specific exception first. Broad catches last, if at all.
- Custom exceptions make errors self-documenting and easier to handle upstream.
- Always use `with open(...)` for file I/O — never rely on manual `.close()`.
- For serious projects, use `pathlib.Path` over raw string paths.
- Never silently swallow exceptions — at minimum, log them.
 