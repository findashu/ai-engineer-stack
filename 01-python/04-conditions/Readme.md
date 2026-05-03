# Python Conditionals

This folder contains Python exercises covering conditionals and decision-making.

## Files and Purpose

- `04-01-kettle-boiling-stry.py`
  - Demonstrates a simple `if` statement with a boolean condition.
  - Prints a notification only when the kettle has finished boiling.

- `04-02-snack-system.py`
  - Uses `input()` and `.lower()` to normalize user input.
  - Demonstrates `if ... else` and logical operators (`or`) to handle multiple valid values.

- `04-03-price-calculator.py`
  - Uses `if`, `elif`, and `else` to select between multiple cup sizes.
  - Shows how to branch logic for mutually exclusive conditions.

- `04-04-smart-thermostat.py`
  - Demonstrates nested conditionals (`if` inside `if`).
  - Handles device status first, then temperature checks only when the device is active.

- `04-05-delevery-fee-waiver-system.py`
  - Uses a ternary expression to decide between free delivery and a fee.
  - Demonstrates concise conditional assignment in Python.

- `04-06-train-ticket-info-system.py`
  - Uses `match` / `case` syntax for pattern matching based on seat type.
  - Provides a clean alternative to long `if` / `elif` chains.

## Important Points

- `if`, `elif`, and `else` are the core tools for decision making in Python.
- Normalize user input with `.lower()` before comparing strings to avoid case-sensitivity issues.
- Use nested `if` statements when one condition depends on another.
- Use a ternary expression (`value_if_true if condition else value_if_false`) for concise conditional assignments.
- `match` / `case` is useful for cleanly handling multiple fixed string options.
- Always validate user input and include an `else` or `case _` fallback for unexpected values.
