# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remain is {remainder}")

# Walrus Operator
value = 13

if (remainder := value %5):
    print(f"Not divisible, remain is {remainder}")

sizes = ["small","medium","large"]

if (req_size := input("Enter the cup size: ")) in sizes:
    print(f"{req_size} is available")
else:
    print(f"{req_size} is not available")



flavours = ["green","mint","ginger"]

print(f"Available flavours: {flavours}")

while (flavour := input("Enter your flavour: ")) not in flavours:
    print(f"{flavour} flavour not available")


print(f"Serving your flavour: {flavour}")
