class Bike:
    wheels = 2
    power = "350 CC"

reborn = Bike()
print("Reborn power:", reborn.power) 
reborn.power = "450 CC"

print("Reborn power after changing:", reborn.power)   
print("Class power:", Bike.power)
reborn.color = "grey"
del reborn.power

print("After deleting:", reborn.power) # picks value from Class (shadowing)
print("Reborn color:", reborn.color)

del reborn.color

#print("After deleting color:", reborn.color) # Error: Has no attribute color