# By default function returns None
# You can return single value
# Or Multiple values

def test_noreturn():
    print("By default will return 'None'")


print(f" Test No return: {test_noreturn()}")

def add (a,b):
    return a+b

print(f"Return single value: {add(2,3)}");

# Break Early

def process_order(itemCount):
    if itemCount == 0:
        return "No item passed"
    return f"Total Count {itemCount}"

print(f"Early Break: {process_order(0)}")
print(f"Final Return: {process_order(5)}")

totalItems = 1000
def inventory(sale):
    remainingItems = totalItems - sale
    return sale,remainingItems

sold, remainingItems = inventory(25)
print(f"Sold: {sold}")
print(f"Remaining: {remainingItems}")