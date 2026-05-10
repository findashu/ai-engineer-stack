
# Infinite Generator:
def serve_infinite():
    count = 1
    while True:
        yield f"Refill count: {count}"
        count += 1

serve = serve_infinite()

# Controlling the infinite generator
for _ in range(5):  # Print first 5 values
    print(next(serve))