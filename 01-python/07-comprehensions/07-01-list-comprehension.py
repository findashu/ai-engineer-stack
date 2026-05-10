# [ expression for item in iterable if condition ]

menu = [
    "Masala Tea",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger Tea"
]

iced_tea = [ tea for tea in menu if "Iced" in tea]

print(iced_tea)