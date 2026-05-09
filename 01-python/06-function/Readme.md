# Python Functions: Comprehensive Guide

This documentation covers Python functions from basic definition to advanced scope management and functional programming concepts. Use this as a reference for your scripts in `01-python/06-function`.

---

## 1. Introduction to Functions
A function is a reusable, named block of code designed to perform a single, specific task. This follows the **DRY (Don't Repeat Yourself)** principle,, making code modular and easier to maintain.

### Basic Syntax
```python
def function_name(parameter1, parameter2):
    """
    Optional Docstring: Explains what the function does.
    """
    # Function body (logic)
    result = parameter1 + parameter2
    return result
```

#### Key-Terms
| Term | Description |
|------|-------------|
| Definition | Creating the function using the `def` keyword. |
| Call / Invoke | Running the function by using its name followed by `()`. |
| Parameters | The placeholders defined in the function signature. |
| Arguments | The actual values passed into the function during a call. |

---

## 2: Arguments & Return Values
Python offers flexible ways to pass data into functions.

### Types of Arguments

- *Positional*: Arguments assigned based on their order.

- *Keyword*: Arguments assigned by name (e.g., `func(name="Ali")`). This makes code more readable.

- *Default Parameters*: Fallback values used if no argument is provided.

* **Pro-tip:** Avoid using mutable objects (like lists `[]`) as default values; use `None` instead

### Variable-length Arguments:

* `*args`: Collects extra **positional** arguments into a **Tuple**.
* `**kwargs`: Collects extra **keyword** arguments into a **Dictionary**.

```python

def make_pizza(size, *toppings, **details):
    print(f"Size: {size}, Toppings: {toppings}, Details: {details}")

make_pizza("Large", "Mushrooms", "Cheese", customer="John", delivery=True)
# Result: toppings=('Mushrooms', 'Cheese'), details={'customer': 'John', 'delivery': True}

```

**File Reference:** `06-07-handling-arguments.py`


---

## 3. Return Values
The `return` statement exits a function and sends a result back to the caller.

* **Single Return:** Returns one value or object.
* **Multiple Returns:** Python can return multiple values separated by commas (returned as a **Tuple**).
* **Early Return:** Use `return` inside an `if` statement to exit a function early (Guard Clause).
* **Implicit None:** If no `return` is specified, Python automatically returns `None`.

**File Reference:** `06-04-return-calculate-bill.py`, `06-08-returns.py`

## 4. Scope and the LEGB Rule
Scope determines where a variable can be accessed. Python searches for variables in this specific order (**LEGB**):

1.  **L (Local):** Inside the current function.
2.  **E (Enclosing):** Inside parent functions (for nested functions).
3.  **G (Global):** At the top level of the script/module.
4.  **B (Built-in):** Pre-defined names like `print()`, `len()`, or `range()`.

### Modifying Scopes

* `global`: Used to modify a module-level variable from inside a function.
* `nonlocal`: Used inside nested functions to modify a variable in the parent function's scope.

[!CAUTION] 
Use global sparingly. Modifying global state makes code harder to debug and test.

**File Reference:** `06-05-scope-named-space.py`, `06-06-nonlocal-global-scope.py`

---

## 5. Functional Programming Tools

### Pure vs. Impure Functions

* **Pure Functions:** Given the same input, they always return the same output and have no "side effects" (they don't change outside variables).
* **Impure Functions:** They interact with the outside world (e.g., modifying a global list or printing to console).

### Lambda Functions
Anonymous, one-line functions used for short-lived logic.
```python
# Syntax: lambda arguments: expression
square = lambda x: x * x
print(square(5)) # 25
```
Commonly used with `map()`, `filter()`, and `sorted()`.

**File Reference:** `06-09-lambdas-pure-impure-fn.py`

### Documentation & Metadata
Good code is self-documenting.

* **Docstrings**: Triple-quoted strings `"""..."""` at the start of a function. Use them to explain the function's purpose. Access them via `help(function_name)` or `function_name.__doc__`.

* **Type Hinting (New!)**: Helps developers understand what data types are expected and returned.
```python
def greet(name: str) -> str:
    return f"Hello {name}"
```

**File Reference:**  `06-10-fun-documents-builtins.py`

### Modules and Packages
As your project grows, you should split functions into different files.

- *Module*: A single `.py` file containing functions.

- *Package*: A folder containing multiple modules and an __init__.py file.(which tells Python to treat the folder as a package).

- *Imports*: Use `import module` or `from module import function`.

- *File Reference*: 06-11-imports-modules-init-file.py
