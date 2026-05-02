# Set in python
# A set is an unordered collection of unique items. It is defined using curly braces {} or the set() constructor. Sets are mutable, meaning you can add or remove items after creation, but they do not allow duplicate elements.

# Creating a set of essential spices for chai
essential_spices = {"cardamom", "clove", "ginger"}
optional_spices = set(["cloves", "nutmeg", "ginger"])
print(f"Essential spices: {essential_spices}")
print(f"Optional spices: {optional_spices}")    

# union of two sets using | operator or union() method
all_spices = essential_spices | optional_spices
print(f"All spices (union): {all_spices}")

# intersection of two sets using & operator or intersection() method
common_spices = essential_spices & optional_spices
print(f"Common spices (intersection): {common_spices}")

only_essential = essential_spices - optional_spices
print(f"Only essential spices (difference): {only_essential}")

# Membership testing - Keyword 'in' is used to check if an element exists in a set
print(f"Is cardamom an essential spice? {'cardamom' in essential_spices}")
print(f"Is nutmeg an essential spice? {'nutmeg' in essential_spices}")

# frozenset is an immutable version of a set, it cannot be modified after creation
frozen_spices = frozenset(["cardamom", "clove", "ginger"])
print(f"Frozen spices: {frozen_spices}")