# Yor're preparing an order summary with customer names and their total bill
# Task:
# Use two lists: one for names and one for bills
# Print: "[Name] paid [amount]

names = ["lallan", "chaudhary", "damru"]
bills = [100,345,444]

for name, bill in zip(names,bills):
    print(f"{name} paid {bill}")