class Car:
    origin = "India" # property

print(Car.origin)
Car.wheels = 4 # adding more property
print(Car.wheels)

# creat object

maruti = Car();


print(f"Maruti origin: {maruti.origin}")

