# How to define
def serve_value():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

stall = serve_value()

for cup in stall:
    print(cup)


def get_order():
    yield "Order 1"
    yield "Order 2"
    yield "Order 3"

orders = get_order() # holds a generator object
# to get the value of first evaluation
print(next(orders)) # Will give first yield
print(next(orders)) # Will give second yield
print(next(orders)) # Will give third yield
# print(next(orders)) # error done with all yield StopIteration

