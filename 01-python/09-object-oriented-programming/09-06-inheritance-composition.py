class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# To inherit a class Pass the parent class name as a parameter: Note: it accepts only classes
class twoWheeler(Vehicle):
    def __init__ (self, engine_size):
        self.engine_size = engine_size



class fourWheeler:
    # Composition (Inherits all the properties of Vehicle) : Holding the class in variable : Note do not call it otherwise it'll return an Object
    new_vehicle = Vehicle

    def __init__(self,power,color):
        self.power = power
        self.color = color
        self.vehicle = self.new_vehicle("Honda", "Civic") # Returns Object of Vehicle Class

    def get_vehicle_info(self):
        return self.vehicle.brand, self.vehicle.model, self.color


classicReborn = twoWheeler(350)

print(classicReborn.engine_size)

new_civic = fourWheeler(200, "Blue")
print(new_civic.get_vehicle_info())
