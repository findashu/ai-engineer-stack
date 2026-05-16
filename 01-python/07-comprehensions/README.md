# Python Comprehensions

Comprehensions are a concise, readable way to build collections from iterables — filtering, transforming, and flattening data in a single expression instead of writing a loop with `.append()`.

---

## Quick Reference

| Type | Syntax | Output |
|---|---|---|
| List | `[expr for x in iterable if cond]` | `list` — ordered, allows duplicates |
| Set | `{expr for x in iterable if cond}` | `set` — unordered, unique values |
| Dict | `{key: val for x in iterable if cond}` | `dict` — key-value pairs |
| Generator | `(expr for x in iterable if cond)` | lazy iterator — values on demand |

All four share the same structure. The only difference is the **bracket type** and whether you have a `key: value` pair.

---

## Anatomy of a Comprehension

```
[  expression   for   variable   in   iterable   if   condition  ]
    ↑ what to       ↑ loop var      ↑ source       ↑ optional filter
      produce
```

- **expression** — what goes into the new collection (can be any Python expression)
- **for variable in iterable** — standard loop
- **if condition** — optional; only include items where this is `True`

---

## 1. List Comprehension

Builds a new list. The most common comprehension type.

```python
numbers = [1, 2, 3, 4, 5]

# Basic — transform every item
squares = [n * n for n in numbers]
# [1, 4, 9, 16, 25]

# With filter — only even numbers
evens = [n for n in numbers if n % 2 == 0]
# [2, 4]

# Transform + filter together
even_squares = [n * n for n in numbers if n % 2 == 0]
# [4, 16]
```

**Equivalent loop for comparison:**
```python
# This is what you're replacing:
even_squares = []
for n in numbers:
    if n % 2 == 0:
        even_squares.append(n * n)
```

📄 `07-01-list-comprehension.py`

---

## 2. Set Comprehension

Like a list comprehension, but wrapped in `{}`. Automatically removes duplicates.

```python
names = ["Anna", "Bob", "anna", "Sam", "bob"]

unique_lower = {name.lower() for name in names}
# {'anna', 'bob', 'sam'}  ← duplicates gone, order not guaranteed
```

Use when you care about **uniqueness**, not order.

📄 `07-02-set-comprehensions.py`

---

## 3. Dictionary Comprehension

Produces a `dict`. Requires a `key: value` expression.

```python
fruits = ["apple", "banana", "cherry"]

# Map each fruit to its length
fruit_lengths = {fruit: len(fruit) for fruit in fruits}
# {'apple': 5, 'banana': 6, 'cherry': 6}

# Flip a dictionary (swap keys and values)
original = {"a": 1, "b": 2, "c": 3}
flipped = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b', 3: 'c'}

# Filter while building
long_fruits = {fruit: len(fruit) for fruit in fruits if len(fruit) > 5}
# {'banana': 6, 'cherry': 6}
```

📄 `07-03-dict-comprehension.py`

---

## 4. Generator Comprehension

Uses `()` instead of `[]`. Does **not** build the full collection in memory — it yields values one at a time (lazy evaluation).

```python
# List comprehension — builds entire list in memory immediately
squares_list = [n * n for n in range(1_000_000)]   # allocates ~8MB

# Generator — computes each value only when asked
squares_gen = (n * n for n in range(1_000_000))    # allocates ~200 bytes

# Consume it
next(squares_gen)       # 0
next(squares_gen)       # 1
list(squares_gen)       # force all values (defeats the purpose)

# Most common use — pass directly to a function
total = sum(n * n for n in range(100))   # no extra brackets needed
```

> Generators are **iterators** — you can only go forward, you can't index them, and once exhausted they're empty.

📄 `07-04-generator-comprehension.py`

---

## Nested Comprehensions

You can nest comprehensions to flatten or transform 2D data.

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Flatten a 2D list
flat = [n for row in matrix for n in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Read order: outer loop first, then inner loop
# for row in matrix → for n in row → take n
```

> 💡 More than **one level of nesting** and you should usually switch to a regular loop — readability tanks fast.

---

## When to Use What

| Situation | Use |
|---|---|
| Build a filtered/transformed list | List comprehension |
| Deduplicate values | Set comprehension |
| Build a lookup table from data | Dict comprehension |
| Large dataset, process one at a time | Generator |
| Passing to `sum()`, `max()`, `any()`, `all()` | Generator (no extra `[]` needed) |
| Complex logic, multiple conditions | Regular `for` loop |

---

## Common Patterns

```python
# 1. Conditional expression (if-else) inside comprehension
labels = ["even" if n % 2 == 0 else "odd" for n in range(5)]
# ['even', 'odd', 'even', 'odd', 'even']

# 2. Call a function on each item
words = ["  hello  ", " world "]
cleaned = [w.strip() for w in words]

# 3. Build a dict from two parallel lists
keys = ["name", "age", "city"]
vals = ["Ashutosh", 30, "Bengaluru"]
profile = {k: v for k, v in zip(keys, vals)}

# 4. any() / all() with generator — short-circuits (stops early)
has_negative = any(n < 0 for n in [1, 2, -3, 4])   # True, stops at -3
all_positive = all(n > 0 for n in [1, 2, -3, 4])   # False, stops at -3
```

---

## Engineer Tips

> 💡 **Readability is the rule.** If you have to pause to understand a comprehension, convert it to a loop. Your future self will thank you.

> 💡 **Generator vs list — default to generator** when passing to `sum()`, `any()`, `all()`, `max()`, `min()`. No `[]` needed and no wasted memory allocation.

> 💡 **Avoid side effects inside comprehensions.** `[print(x) for x in items]` works but is an abuse of the pattern. Comprehensions are for building values, not for running side effects — use a `for` loop for that.

> 💡 **Dict comprehension for fast lookups.** If you're doing repeated `if item in list` checks in a loop, convert the list to a set or dict first:
> ```python
> # ❌ O(n) lookup every iteration
> if user_id in allowed_ids_list:  ...
>
> # ✅ O(1) lookup — build once, query many times
> allowed = {uid: True for uid in allowed_ids_list}
> if user_id in allowed: ...
> ```

> 💡 **`walrus operator` (`:=`) in comprehensions (Python 3.8+).** Lets you compute a value and reuse it without computing it twice:
> ```python
> # Without walrus — len() called twice
> filtered = [s for s in strings if len(s) > 3 and len(s) < 10]
>
> # With walrus — compute once, reuse
> filtered = [s for s in strings if 3 < (n := len(s)) < 10]
> ```

---

## Key Takeaways

- All four types share the same `[expr for x in iterable if cond]` structure — only the brackets differ.
- List = ordered + allows duplicates. Set = unique. Dict = key-value. Generator = lazy.
- Read nested comprehensions as: **outermost loop first**, then inner.
- Generators save memory — use them when feeding `sum()`, `any()`, `all()` or processing large data.
- If it doesn't read naturally in one pass — use a loop.