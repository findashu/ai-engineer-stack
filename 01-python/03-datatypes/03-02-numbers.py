# Integer 
import sys
from decimal import Decimal
black_tea_grams = 14
ginger_grams = 5
total_grams = black_tea_grams + ginger_grams
print(f"Total grams: {total_grams}")

milk_liters = 7
servings = 4
milk_per_serving = milk_liters / servings
print(f"Milk per serving: {milk_per_serving} liters")

# Float
price_per_kg = 2.5
weight_kg = 3.2
total_cost = price_per_kg * weight_kg
print(f"Total cost: ${total_cost:.2f}")

print(f"Float Info: {sys.float_info}")

# Complex
a = 2 + 3j
b = 1 - 4j
c = a + b
print(f"Result of adding complex numbers: {c}")

#Remainder
dividend = 10
divisor = 3
remainder = dividend % divisor
print(f"Remainder of {dividend} divided by {divisor} is: {remainder}")

# exponentiation
base = 5
exponent = 3
result = base ** exponent
print(f"{base} raised to the power of {exponent} is: {result}")

bignumber_readable_way = 1_000_000_000
print(f"Another way to write one billion: {bignumber_readable_way}") 



# Booleans

is_raining = True
is_sunny = False    
print(f"Is it raining? {is_raining}")
print(f"Is it sunny? {is_sunny}")

#upcasting (True is treated as 1 and False as 0 in arithmetic operations)
is_boiling = True
stri_count = 5
total_actions = is_boiling + stri_count
print(f"Total actions (upcasting boolean to integer): {total_actions}")

milk_present = 1 
print(f"Is milk present? {bool(milk_present)}")

#Logical operations
is_weekend = True
is_holiday = False
can_relax = is_weekend and is_holiday
print(f"Can I relax? {can_relax}")