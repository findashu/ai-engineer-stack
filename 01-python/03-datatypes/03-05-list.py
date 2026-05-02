# List basically is a collection of items. It is ordered and changeable. It allows duplicate members. Its mutable nature means that we can change the content of a list after it has been created. Lists are defined by having values between square brackets [ ]. like array in other programming languages.

ingredients = ["Tea Leaves", "Water", "Milk"]
print(f"Ingredients: {ingredients}")
# Adding an item to the list using append() method
ingredients.append("Sugar")
print(f"Ingredients after adding sugar: {ingredients}")
# Removing an item from the list using remove() method
ingredients.remove("Water")
print(f"Ingredients after removing water: {ingredients}")
# Accessing items in the list using indexing
first_ingredient = ingredients[0]
print(f"First ingredient: {first_ingredient}")
# Slicing the list to get a subset of ingredients
subset_ingredients = ingredients[0:2]
print(f"Subset of ingredients: {subset_ingredients}")
# Reversing the list using slicing
reversed_ingredients = ingredients[::-1]
print(f"Reversed ingredients: {reversed_ingredients}")

# Few other important list methods
# insert() method to add an item at a specific index
ingredients.insert(1, "Cardamom")
print(f"Ingredients after inserting cardamom at index 1: {ingredients}")
# pop() method to remove an item at a specific index (default is the last item) and return it
removed_ingredient = ingredients.pop(2)
print(f"Removed ingredient: {removed_ingredient}")
print(f"Ingredients after popping index 2: {ingredients}")
# clear() method to remove all items from the list
ingredients.clear()
print(f"Ingredients after clearing the list: {ingredients}")

options = ["Regular", "Masala", "Ginger"]
chai_ingredients = ['water', 'milk', 'tea leaves', 'sugar']
# Extending a list with another list using extend() method
options.extend(chai_ingredients)
print(f"Options after extending with chai ingredients: {options}")  

# Reverse the list using reverse() method, it does not return a new list but modifies the original list in place
options.reverse()
print(f"Options after reversing: {options}")

# Sorting a list using sort() method, it sorts the list in place and does not return a new list
options.sort()
print(f"Options after sorting: {options}")

sugar_levels = [5, 2, 8, 1, 4]
# Find the maximum and minimum sugar levels using max() and min() functions
max_sugar = max(sugar_levels)
min_sugar = min(sugar_levels)
print(f"Maximum sugar level: {max_sugar}")
print(f"Minimum sugar level: {min_sugar}")

# Operator overloading with lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# Concatenation using + operator
concatenated_list = list1 + list2
print(f"Concatenated list: {concatenated_list}")
# Repetition using * operator
repeated_list = list1 * 3
print(f"Repeated list: {repeated_list}")    


# byteary data type
label = bytearray("Chai Special", 'utf-8')
print(f"Encoded label: {label}")

label = label.replace(b'Special', b'Premium')
print(f"Modified label: {label}")   
