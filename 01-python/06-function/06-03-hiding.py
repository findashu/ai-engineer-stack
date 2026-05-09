# Hiding Implementation Details
# You are building an app that registers users
# You want to seperate concerns: getting input, validating it and saving it
# Task:
# Write register user() that calls:
# get_input()
# validate_input()
# save_to_db()

def get_input():
    print("Getting user input")

def validate_input():
    print("Validating user input")

def save_to_db():
    print("Saving user data to db")
          
def register_user():
    get_input()
    validate_input()
    save_to_db()
    print("User registered")

register_user()