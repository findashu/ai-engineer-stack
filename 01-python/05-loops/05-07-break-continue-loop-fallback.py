# Some ingredients are out of stock
# You want to skip those and stop entirely if someone requests a restricted ingredient
# Task:
# Skip if ingredient is out of stock
# Break if ingredient is discontinued

ingredients = ["ginger","out of stock","mint","discontinued","black"]

for ingredient in ingredients:
    if ingredient == "out of stock":
        continue
    elif ingredient == "discontinued":
        print(f"{ingredient} Ingredient found")
        break
    print(f"{ingredient} Ingredient found")
    
        
print(f"Out of loop")

