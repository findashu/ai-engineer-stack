# nonlocal - Looks one above from its scope

def update_order():
    order_type = "online"
    def kitchen():
        nonlocal order_type
        order_type = "offline"
    kitchen()
    print(f"After kitchen update: {order_type}")

update_order()
# print(f"{order_type}") doesn't make it global

# global - global object 

status = "order taken"
def order_status():
    def kitchen():
        global status
        status = "cooked"
    kitchen()

order_status()
print(f"Final Status: {status}")
