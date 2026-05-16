class Building:
    floor = 5
    parking = "Underground"

    def describe (self):
        return f"This building has {self.floor} floors and {self.parking} parking."


antilla = Building()
print(antilla.describe()) # Context gets passed when method via object
#print(Building.describe()) # Error as there's no context
print(Building.describe(antilla)) # Same as above, but more explicit context being passed


