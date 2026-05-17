def process_order(item,quantity):
    try:
        price = {"latte": 3.50, "cappuccino": 4.00, "espresso": 3.00}[item]
        cost = price * quantity
        print(f"Order processed. Total cost: ${cost:.2f}")
    except KeyError:
        print("Sorry that coffee is not available")
    except TypeError:
        print("Quantity must be a number")
    
process_order("latte", 2)
process_order("unknown",2)
process_order("espresso", "2")
process_order("unknown", "two") # throws first exception