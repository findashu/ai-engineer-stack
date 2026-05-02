# Tuples are Immutable sequences of elements, similar to lists but with a fixed size and type. They can be defined using parentheses ().
chai_flavors = ("Regular", "Masala", "Ginger")
print(f"Available chai flavors: {chai_flavors}")

# Seperate them into individual variables (unpacking)
flavour1, flavour2, flavour3 = chai_flavors
print(f"Regular flavor: {flavour1}")

ginger_ratio, cardamom_ratio, clove_ratio = 0.5, 0.3, 0.2
print(f"Ginger ratio: {ginger_ratio}, Cardamom ratio: {cardamom_ratio}, Clove ratio: {clove_ratio}")

#Swapping values without a temporary variable
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"After swapping - Ginger ratio: {ginger_ratio}, Cardamom ratio: {cardamom_ratio}")

# Membership testing - Keyword 'in' is used to check if an element exists in a tuple
print(f"Is 'Masala' flavor available? {'Masala' in chai_flavors}")
# it's case sensitive, so 'masala' will not be found in the tuple
print(f"Is 'Masala' flavor available? {'masala' in chai_flavors}")

#Indexing
# Tuples are indexed starting from 0. You can access individual elements using their index.
first_flavor = chai_flavors[0]
print(f"First flavor: {first_flavor}")

# Slicing
# You can extract a subset of elements using slicing. The syntax is tuple[start:end:step], where start is the index to start from (inclusive) and end is the index to end at (exclusive).
subset_flavors = chai_flavors[0:2]
print(f"Sliced flavors: {subset_flavors}")

#Reversing a tuple using slicing
reversed_flavors = chai_flavors[::-1]
print(f"Reversed flavors: {reversed_flavors}")