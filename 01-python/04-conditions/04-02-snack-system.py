# A local cafe wants a program that suggests snack.
# If a customer asks for cookies or samosha, it confirms the order #otherwise
# it says it's not available. Tasks:
# Take snack input
# If it's 'cookies' or 'samosa', confirm the order
# Else, show unavailability

snack = input("Enter your preferred snack: ").lower()

print(f"User ordered: {snack}")

if snack == "cookies" or snack == "samosa":
    print(f"Great Choice! Will serve you {snack}")
else:
    print(f"Sorry, we only serve cookies or samosa with tea ")
