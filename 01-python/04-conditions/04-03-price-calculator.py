# A tea stall offers different prices for different cup sizes
# Write a program that calculates the price based on size
# Task:
# Input: "small", "medium", "large"
# Prices: small = 10, medium = 15, large = 20
# If invalid show 'unknown cup size'

cup = input(f"Enter cup size (small/medium/large): ").lower()

if cup == "small":
    print(f"Price is 10")
elif cup == "medium":
    print(f"Price is 15")
elif cup == "large":
    print(f"Price is 20")
else:
    print(f"Unknown cup size")