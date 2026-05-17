class InvalidCoffeeError(Exception):pass

def bill(flavour, cups):
    menu = {"latte": 20, "espresso": 30, "cappuccino": 40}
    try:
        if flavour not in menu:
            raise InvalidCoffeeError("Invalid coffee type.")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an integer")
        total = menu[flavour] * cups
        print(f"Total bill for {cups} cups of {flavour}: ${total}")
    except Exception as e:
        print(f"Error: {e}")


bill("latte", 3)
bill("latte", "3")
bill("unknown", "3")