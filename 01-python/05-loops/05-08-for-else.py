staff = [("Amit",16),("Taman",11),("Jogi",12)]

for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible to hire");
        break;
else:
    print("No match found")