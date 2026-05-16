class MultiOrder:
    def __init__(self, order_id, customer_name):
        self.order_id = order_id
        self.customer_name = customer_name
    
    @classmethod
    def fromDict(cls, order_dict):
        return cls(
            order_id=order_dict["order_id"],
            customer_name=order_dict["customer_name"]
        )

    @classmethod
    def fromString(cls, order_str):
        order_id, customer_name = order_str.split(",")
        return cls(
            order_id=order_id.strip(),
            customer_name=customer_name.strip()
        )
    

order1 = MultiOrder.fromDict({"order_id": "1", "customer_name": "John Doe"})
order2 = MultiOrder.fromString("2, Jane Smith")

print(order1.__dict__)
print(order2.customer_name)


class Utils:

    @staticmethod
    def is_valid_size(size):
        return size in ["small", "medium", "large"]