# Variable with initial value
sugar_amount = 30
print(f"Initial value of Sugur: {sugar_amount}")

# same variable with different
sugar_amount = 50
print(f"Second value of Sugur: {sugar_amount}")

# What happens, value doesn't gets changed reference of the value stored in memory changes - immutable (value not changed - variable started pointing another space), below prints actual identity where its stored
# Example Number : Immutable
print(f"Id of 1: {id(30)}")
print(f"Id of 2: {id(50)}")

# Mutable Example of Sets

spice_mix = set()

print(f"Id of spice_mix: {id(spice_mix)}")
print(f"Initial spice_mix: {spice_mix}")
spice_mix.add("ginger")
spice_mix.add("cardmom")
print(f"Id of spice_mix after change: {id(spice_mix)}")
print(f"After addition spice_mix: {spice_mix}")

