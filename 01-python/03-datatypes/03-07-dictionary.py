# Dictionary in python
# A dictionary is an unordered collection of key-value pairs. It is defined using curly braces {} with keys and values separated by a colon (:). Dictionaries are mutable, meaning you can add, remove, or change items after creation. Keys must be unique and immutable (like strings, numbers, or tuples), while values can be of any data type.

chai_order = dict(customer="John Doe", flavor="Masala", sugar_level=5)
print(f"Chai order: {chai_order}")
# Accessing values in a dictionary using keys
customer_name = chai_order["customer"]
print(f"Customer name: {customer_name}")
print(f"Chai flavor: {chai_order['flavor']}")

# Adding a new key-value pair to the dictionary
chai_order["milk_type"] = "Whole"
print(f"Chai order after adding milk type: {chai_order}")
# Modifying an existing value in the dictionary
chai_order["sugar_level"] = 3
print(f"Chai order after modifying sugar level: {chai_order}")
# Removing a key-value pair from the dictionary using del keyword
del chai_order["milk_type"]
print(f"Chai order after removing milk type: {chai_order}")
# Removing a key-value pair from the dictionary using pop() method, it also returns the value
removed_flavor = chai_order.pop("flavor")
print(f"Removed flavor: {removed_flavor}")
print(f"Chai order after popping flavor: {chai_order}")

# Membership testing - Keyword 'in' is used to check if a key exists in a dictionary
print(f"Is 'customer' key in chai order? {'customer' in chai_order}")
print(f"Is 'flavor' key in chai order? {'flavor' in chai_order}")


chai_order2 = {"customer": "Jane Smith", "flavor": "Ginger", "sugar_level": 2}
# Printing all keys and values in the dictionary
print(f"Chai order 2: {chai_order2}")
print(f"Keys in chai order 2: {chai_order2.keys()}") 
print(f"Values in chai order 2: {chai_order2.values()}")
print(f"Items in chai order 2: {chai_order2.items()}")

# Updating a dictionary with another dictionary using update() method, it adds new key-value pairs and updates existing keys
chai_order.update(chai_order2)
print(f"Chai order after updating with chai order 2: {chai_order}")

# get() method to access values in a dictionary, it returns None if the key does not exist instead of raising an error get(key, message) - you can also provide a custom message to return if the key is not found
customer = chai_order.get("customer")
print(f"Customer from get() method: {customer}")
non_existent_key = chai_order.get("non_existent_key", "Key not found")
print(f"Non-existent key from get() method: {non_existent_key}")