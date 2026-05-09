# Calculate the bill
# WAF that takes number of items and price per item 
# return total amount

def calculate_bill(totalItem, pricePerItem):
    return totalItem * pricePerItem

mybill = calculate_bill(12,3)
print(f"Total bill is {mybill}")
print(f"Total bill is {calculate_bill(13,5)}")

# Improving Traceability
# A shop adds 10% VAT on every order
# You want this to be consistent and traceable
# Task:
# Write vat_price(price,vat_rate)
# Use it to compute final prices for 3 orders

def vat_price(price,vat_rate):
    return price * (100 + vat_rate)/100

orders = [100,150,200]

for order in orders:
    print(f"Final Price, {vat_price(order,10)}")