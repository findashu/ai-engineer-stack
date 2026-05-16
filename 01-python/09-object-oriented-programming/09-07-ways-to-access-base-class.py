class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


# Way 1: Kind of code duplication
# class Mobile(Device):
#     def __init__(self, brand, model, storage):
#         self.brand = brand
#         self.model = model
#         self.storage = storage

# Way 2: Explicit Call: Using Device.__init__() to access the base class : 
class Mobile(Device):
    def __init__(self, brand, model, storage):
        Device.__init__(self, brand, model)
        self.storage = storage

# Way 3: super(): Using super()
class Tab(Device):
    def __init__(self, brand, model, screen_size):
        super().__init__(brand, model)
        self.screen_size = screen_size