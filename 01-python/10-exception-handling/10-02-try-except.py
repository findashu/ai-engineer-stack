employee = {"name": "John", "age": 30}

try:
    employee["lastname"]
except KeyError: # as we know the error type
    print("Last name not found")

print("End Program")