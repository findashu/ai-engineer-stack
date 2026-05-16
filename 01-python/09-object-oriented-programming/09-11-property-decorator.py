class Calculate:
    def __init__(self, price):
        self._price = price
    
    # getter
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if 1 <= value <= 100:
            self._price = value
        else:
            raise ValueError("Price must be between 1 and 100")
        


calc = Calculate(50)

print(calc.price)

calc.price = 75
print(calc.price)

# calc.price = 150 Error