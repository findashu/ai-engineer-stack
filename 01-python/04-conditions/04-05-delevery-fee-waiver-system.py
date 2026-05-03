# You run an online store
# If the order amount is more than 300, delivery is free 
# otherwise; it costs 30
# Task:
# Input: 'order_amount'
# Use ternary operator to decide delivery fee

order_amount = int(input("Enter Order Amount :"))

delivery_fee = 0 if order_amount > 300 else 30

print(f"Delivery fee: {delivery_fee}")