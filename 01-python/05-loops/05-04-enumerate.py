# You are creating a menu board
# Each item must be numbered
# Task:
# Use enumerate() to print menu items with numbers

menu = ["tea","coffee","chakli","bread","biscuit"]

for idx, item in enumerate(menu, start=1):
    print(f"Menu Item {idx}:{item}")