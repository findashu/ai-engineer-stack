# Comprehensions

Python comprehensions provide a concise, readable way to build new collections from existing iterables. They are especially useful for filtering, transforming, and flattening data in a single expression.

## Why use comprehensions?

- Cleaner code compared to loops
- More expressive intent
- Often faster than equivalent manual loops
- Great for creating lists, sets, dictionaries, or generators quickly

## Types of comprehensions

- **List comprehension** — build lists
- **Set comprehension** — build sets
- **Dictionary comprehension** — build dictionaries
- **Generator comprehension** — build generators lazily

## Common use cases

- filtering values from an iterable
- transforming items with a function or expression
- flattening nested lists
- building lookup dictionaries from data
- generating values on demand with a generator

## Examples

### List comprehension

```python
numbers = [1, 2, 3, 4, 5]
squares = [n * n for n in numbers]
```

### Set comprehension

```python
names = ["Anna", "Bob", "Anna", "Sam"]unique_names = {name.lower() for name in names}
```

### Dictionary comprehension

```python
items = ["apple", "banana", "cherry"]fruit_map = {item: len(item) for item in items}
```

### Generator comprehension

```python
even_generator = (n for n in range(10) if n % 2 == 0)
```

## Learn more in these lesson files

- `07-01-list-comprehension.py` — list comprehension basics
- `07-02-set-comprehensions.py` — set comprehension examples
- `07-03-dict-comprehension.py` — dictionary comprehension patterns
- `07-04-generator-comprehension.py` — generator expression usage

## Best practices

- Use comprehensions when they remain readable
- Avoid deeply nested comprehensions if the logic becomes hard to follow
- Prefer list comprehensions for simple mapping and filtering
- Use generator comprehensions when you need lazy evaluation
