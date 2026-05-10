def cafe():
    yield "Coffee"
    yield "Tea"
    yield "Juice"

# Using yield from to delegate to another generator
def snacks():
    yield "Chips"
    yield "Biscuits"
    yield "Water"

def full_menu():
    yield from cafe()
    yield from snacks()

for item in full_menu():
    print(item)

def stall():
    try:
        while True:
            order = yield
    except:
        print("Stall closed")

new_stall = stall();

print(next(new_stall))

new_stall.close() # Stopping the generator, cleaning up memory


