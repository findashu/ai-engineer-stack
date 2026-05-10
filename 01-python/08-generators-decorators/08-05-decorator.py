from functools import wraps # tool to keep function metadata

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator # adding decorator, if remove function will work as normal
def greet():
    print("Hello, World!")

greet()
print(greet.__name__) # by adding wraps - will get greet