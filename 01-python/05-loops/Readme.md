# Loops in Python

This section covers various types of loops and loop control mechanisms in Python, along with related functions and operators.

## 05-01-token-dispenser.py
Simulates a token dispenser system where tokens are issued sequentially from 1 to 10.

**New Concepts:**
- `for` loop: Used to iterate over a sequence.
- `range(start, stop)`: Generates a sequence of numbers from start to `stop-1`.

## 05-02-batch-job.py
Simulates preparing bread batches every 15 minutes for 4 batches.

**New Concepts:**
- `for` loop: Iterates over a range of batch numbers.
- `range(start, stop)`: Creates a sequence for batch numbers 1 to 4.

## 05-03-loop-list.py
Demonstrates iterating over a list of customer names to print order readiness.

**New Concepts:**
- `for` loop: Iterates directly over list elements.

## 05-04-enumerate.py
Creates a numbered menu board using enumeration.

**New Concepts:**
- `enumerate(iterable, start=1)`: Returns an enumerate object that yields pairs (index, item) for each item in the iterable, starting from the specified start value.

```python

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
list(enumerate(seasons, start=1))
# [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

```

## 05-05-zip-can-comine-list.py
Combines customer names with their bill amounts for order summary.

**New Concepts:**
- `zip(*iterables)`: Takes iterables and returns an iterator of tuples where the i-th tuple contains the i-th element from each of the argument sequences.

```python

for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):
    print(item)

(1, 'sugar')
(2, 'spice')
(3, 'everything nice')

```

## 05-06-while-loop.py
Simulates heating coffee from 40°C to boiling point (100°C) in steps.

**New Concepts:**
- `while` loop: Executes as long as the condition is true.

## 05-07-break-continue-loop-fallback.py
Handles ingredient processing with skip and stop conditions.

**New Concepts:**
- `continue`: Skips the rest of the current iteration and moves to the next one.
- `break`: Terminates the loop entirely.

## 05-08-for-else.py
Checks staff eligibility with a fallback if no one qualifies.

**New Concepts:**
- `for-else`: The else block executes only if the loop completes normally (without break).

## 05-09-walrus-operator.py
Uses the walrus operator for assignment within expressions.

**New Concepts:**
- Walrus operator `:=`: Assigns values to variables as part of a larger expression (assignment expression).

## 05-10-dictionary-use.py
Applies discounts using a dictionary lookup for coupon codes.

**New Concepts:**
- Dictionary: A collection of key-value pairs.
- `dict.get(key, default)`: Returns the value for key if key is in the dictionary, else default.