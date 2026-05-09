# Scopes and Name Resolution
# Local Scope: Inside the function
# Enclosing from outer function if nested
# Global - Top level script
# Built in

def inside_scope():
    inside_name = "Java" # function scope
    print(f"function scope variable: {inside_name}")
    print(f"Inside function access global: {outside_name}")

outside_name = "bablu" # global scope
# print(f"Access function variable in global {inside_name}") // Error
print(f"Access global variable in global {outside_name}")

inside_scope()

# Enclosing

def outer_function():
    outOrder = "out placed" # Enclosing scope
    def inner_func():
        innerorder = "inner placed"
        print(f"Inner Order: {innerorder}")
        print(f"Outer function Order: {outOrder}")
    inner_func()
#    print(f"Outer func order: {innerorder}") Error
    print(f"Outer func order: {outOrder}")

outer_function()
    


