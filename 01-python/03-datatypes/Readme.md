# Data Types and Mutability

This section explores Python's built-in data types and the concept of mutability, which is fundamental to understanding how Python manages data in memory.

## Everything is an Object

In Python, everything is an object. Each object has three key properties:
- **Identity**: A unique identifier (memory address)
- **Type**: The object's type (int, str, list, etc.)
- **Value**: The actual data stored

You can check these with built-in functions:
```python
x = 42
print(id(x))    # Identity
print(type(x))  # Type
print(x)        # Value
```

## Mutability

### Mutable vs Immutable

- **Mutable**: Objects whose value can be changed after creation
- **Immutable**: Objects whose value cannot be changed after creation

The identity determines mutability, not the value. If you "change" an immutable object, you're actually creating a new object with a new identity.

### Immutable Examples

Numbers, strings, and tuples are immutable:

```python
# Numbers are immutable
sugar_amount = 30
print(f"Initial value: {sugar_amount}, ID: {id(sugar_amount)}")

sugar_amount = 50  # This creates a new object
print(f"New value: {sugar_amount}, ID: {id(sugar_amount)}")
```

### Mutable Examples

Lists, dictionaries, and sets are mutable:

```python
# Sets are mutable
spice_mix = set()
print(f"Initial ID: {id(spice_mix)}")
print(f"Initial set: {spice_mix}")

spice_mix.add("ginger")
spice_mix.add("cardamom")
print(f"After changes ID: {id(spice_mix)}")  # Same ID!
print(f"Modified set: {spice_mix}")
```

## Important Concepts and Theories

### Python's Object Model

Python follows a consistent object model where:
- **Everything is an object**: Even basic types like integers are objects
- **Objects have reference semantics**: Variables hold references to objects, not the objects themselves
- **Identity vs Equality**: `is` checks identity, `==` checks equality
- **Garbage collection**: Automatic memory management based on reference counting

### Memory Management

- **Immutable objects**: Can be safely shared between variables (interning for small integers/strings)
- **Mutable objects**: Changes affect all references to the same object
- **Copy vs Reference**: Understanding when you're copying data vs. sharing references

### Performance Considerations

- **Lists vs Tuples**: Lists are slower for iteration, tuples are faster and use less memory
- **Sets vs Lists**: Sets provide O(1) lookup vs O(n) for lists
- **Dictionaries**: Highly optimized hash tables with O(1) average-case operations
- **String operations**: Immutable strings mean concatenation creates new strings (use join() for efficiency)

## Numeric Types

Python supports several numeric types, all of which are immutable.

### Integers (int)

Whole numbers without decimal points. In Python 3, integers can be arbitrarily large.

**Key Points:**
- Unlimited precision (no overflow like in C/Java)
- Efficient storage for small integers (-5 to 256 are interned)
- Support for binary, octal, hexadecimal literals

```python
# Basic arithmetic
black_tea_grams = 14
ginger_grams = 5
total_grams = black_tea_grams + ginger_grams
print(f"Total grams: {total_grams}")

# Remainder and exponentiation
remainder = 10 % 3
result = 5 ** 3
print(f"Remainder: {remainder}, 5^3: {result}")

# Large numbers with underscores for readability
bignumber = 1_000_000_000
```

### Floating-Point Numbers (float)

Double-precision floating-point numbers (IEEE 754 standard).

**Key Points:**
- Limited precision (about 15 decimal digits)
- Represented as `float` type
- Special values: `inf`, `-inf`, `nan`
- Use `decimal.Decimal` for financial calculations requiring exact decimal representation

```python
milk_liters = 7
servings = 4
milk_per_serving = milk_liters / servings
print(f"Milk per serving: {milk_per_serving} liters")

price_per_kg = 2.5
weight_kg = 3.2
total_cost = price_per_kg * weight_kg
print(f"Total cost: ${total_cost:.2f}")
```

### Complex Numbers (complex)

Numbers with real and imaginary parts.

**Key Points:**
- Represented as `real + imaginary j`
- Useful for mathematical computations, signal processing
- Access real/imaginary parts with `.real` and `.imag` attributes

```python
a = 2 + 3j
b = 1 - 4j
c = a + b
print(f"Result: {c}")
```

### Booleans (bool)

True or False values. Subclass of int (True = 1, False = 0).

**Key Points:**
- Result of comparison operations
- Can be used in arithmetic (True + True = 2)
- Falsy values: None, 0, 0.0, '', [], {}, set(), etc.

```python
is_raining = True
is_sunny = False
print(f"Is it raining? {is_raining}")
```

## Sequence Types

### Strings (str) - Immutable

Sequences of Unicode characters used for text data.

**Key Points:**
- Immutable: operations create new strings
- Unicode support by default
- String methods return new strings, don't modify in-place
- Use f-strings for efficient string formatting (Python 3.6+)

```python
# String definition
chai_type = "Normal Chai"
customer_name = 'John Doe'
chai_description = "Aromatic and Bold"

# String formatting
print(f"Order for {customer_name}: {chai_type}")

# Indexing and slicing
first_char = chai_description[0]
substring = chai_description[0:9]
skipped = chai_description[0:9:2]  # Skip every second character

# Reversing
reversed_str = chai_description[::-1]

# Encoding/decoding
encoded = chai_description.encode('utf-8')
decoded = encoded.decode('utf-8')
```

### Tuples - Immutable

Ordered, immutable sequences of elements.

**Key Points:**
- Immutable: cannot be modified after creation
- Can be used as dictionary keys (unlike lists)
- Unpacking allows multiple assignment
- Often used for returning multiple values from functions
- Slightly more memory efficient than lists

```python
# Tuple definition
chai_flavors = ("Regular", "Masala", "Ginger")

# Unpacking
flavour1, flavour2, flavour3 = chai_flavors

# Swapping values
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio

# Membership testing
print("Masala" in chai_flavors)

# Indexing and slicing
first_flavor = chai_flavors[0]
subset = chai_flavors[0:2]
reversed_tuple = chai_flavors[::-1]
```

### Lists - Mutable

Ordered, mutable sequences that allow duplicates.

**Key Points:**
- Mutable: can be modified in-place
- Dynamic sizing: automatically resize as needed
- Support for mixed data types
- List comprehensions for efficient creation
- Common operations: append, extend, insert, remove, pop, sort

```python
# List definition
ingredients = ["Tea Leaves", "Water", "Milk"]

# Adding/removing items
ingredients.append("Sugar")
ingredients.remove("Water")

# Indexing and slicing
first_ingredient = ingredients[0]
subset = ingredients[0:2]
reversed_list = ingredients[::-1]

# Other methods
ingredients.insert(1, "Cardamom")
removed = ingredients.pop(2)
ingredients.clear()

# Extending and sorting
options = ["Regular", "Masala", "Ginger"]
options.extend(ingredients)
options.reverse()
options.sort()

# Built-in functions
sugar_levels = [5, 2, 8, 1, 4]
max_sugar = max(sugar_levels)
min_sugar = min(sugar_levels)
```

## Set Types

### Sets - Mutable

Unordered collections of unique items.

**Key Points:**
- Unordered: no indexing or slicing
- Unique elements: duplicates automatically removed
- Fast membership testing (O(1) average case)
- Support for mathematical set operations
- Cannot contain mutable objects (lists, dicts)

```python
# Set definition
essential_spices = {"cardamom", "clove", "ginger"}
optional_spices = set(["cloves", "nutmeg", "ginger"])

# Set operations
all_spices = essential_spices | optional_spices  # Union
common_spices = essential_spices & optional_spices  # Intersection
only_essential = essential_spices - optional_spices  # Difference

# Membership testing
"cardamom" in essential_spices
```

### Frozensets - Immutable

Immutable version of sets.

**Key Points:**
- Immutable: can be used as dict keys or set elements
- Same operations as sets (union, intersection, etc.)
- Hashable, unlike regular sets

```python
frozen_spices = frozenset(["cardamom", "clove", "ginger"])
```

## Mapping Types

### Dictionaries (dict) - Mutable

Unordered collections of key-value pairs.

**Key Points:**
- Keys must be hashable (immutable)
- Values can be any type
- Highly optimized hash table implementation
- Dict comprehensions for creation
- Ordered in Python 3.7+ (insertion order preserved)

```python
# Dictionary definition
chai_order = dict(customer="John Doe", flavor="Masala", sugar_level=5)
# or
chai_order = {"customer": "John Doe", "flavor": "Masala", "sugar_level": 5}

# Accessing values
customer_name = chai_order["customer"]

# Adding/modifying items
chai_order["milk_type"] = "Whole"
chai_order["sugar_level"] = 3

# Removing items
del chai_order["milk_type"]
removed_flavor = chai_order.pop("flavor")

# Membership testing
"customer" in chai_order

# Dictionary methods
keys = chai_order.keys()
values = chai_order.values()
items = chai_order.items()

# Updating
chai_order.update({"size": "Large"})

# Safe access
customer = chai_order.get("customer")
not_found = chai_order.get("non_existent", "Key not found")
```

## Advanced Data Types

Python includes several advanced data types for specialized use cases:

### Date and Time (datetime module)

For handling dates, times, and time intervals.

### Collections

Specialized container datatypes:

```python
from collections import namedtuple

# Named tuples for structured data
ChaiOrder = namedtuple('ChaiOrder', ['customer_name', 'chai_type', 'sugar_level'])
order1 = ChaiOrder(customer_name="John Doe", chai_type="Masala", sugar_level=5)
print(f"Order: {order1}")
```

### Third-Party Libraries

Libraries like `arrow` provide enhanced date/time functionality:

```python
import arrow

brewing_time = arrow.utcnow()
print(f"Brewing time: {brewing_time}")
```

## Best Practices and Common Pitfalls

### Choosing the Right Data Type

- **Use tuples for immutable sequences**: When data shouldn't change
- **Use lists for dynamic collections**: When you need to add/remove items
- **Use sets for unique items**: When duplicates don't matter and fast lookup is needed
- **Use dicts for key-value relationships**: When you need to associate data

### Common Mistakes

- **Modifying while iterating**: Don't modify lists/dicts while iterating over them
- **Mutable default arguments**: Avoid `def func(arg=[])` - use `None` instead
- **String concatenation in loops**: Use `''.join()` instead of `+=` for efficiency
- **Using lists as dict keys**: Lists aren't hashable - use tuples instead

### Type Hints (Python 3.5+)

Modern Python supports type annotations for better code clarity:

```python
from typing import List, Dict, Tuple

def process_order(order: Dict[str, str], ingredients: List[str]) -> Tuple[str, int]:
    # Function implementation
    pass
```

## Why Mutability Matters

Understanding mutability helps you:
- Avoid unexpected side effects when modifying shared objects
- Write more efficient code
- Debug issues with object references
- Choose appropriate data structures for your use case

## Code Examples

See the following files for complete code examples:
- `03-01-mutability.py` - Mutability concepts
- `03-02-numbers.py` - Numeric types
- `03-03-string.py` - String operations
- `03-04-tuples.py` - Tuple operations
- `03-05-list.py` - List operations
- `03-06-set.py` - Set operations
- `03-07-dictionary.py` - Dictionary operations
- `03-08-advance-datatype.py` - Advanced data types

