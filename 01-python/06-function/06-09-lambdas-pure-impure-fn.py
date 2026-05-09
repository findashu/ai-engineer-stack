# Types of Functions
# Pure Vs Impure 
# Recursive
# Lambdas (anonymous functions)

# Pure functions which doesn't manipulate golabal variables

# pure
total_items = 10
def pure_fn(itemCount):
    return itemCount *10

# Not recommended
def impure_fn(itemCount):
    global total_items
    global_items += itemCount

# Recursive

def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    return  n * recursive_factorial(n-1)

print(recursive_factorial(5))


# Lambda Functions

bornList = [1933,1834,1947,1960,1879]

filterEighteens = list(filter(lambda yr: yr < 1899, bornList ))
print(filterEighteens)
