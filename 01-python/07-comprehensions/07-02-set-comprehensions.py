# {expression for item in iterable if condition}

bucket = ["apple", "mango", "grapes","tomato","apple","potato","biscuits","mango"]

unique_products = {product for product in bucket }
unique_products2 = {product for product in bucket if len(product) >5 }

print(unique_products)
print(unique_products2)

receipes = {
    "paneer":["paneer","turmeric","redchilli","black pepper"],
    "kofta":["turmeric","veggies"],
    "mushroom":["mushroom", "black pepper", "greenchilli","coriander"]
}

unique_ingredients = {spice for ingredients in receipes.values() for spice in ingredients }

print(unique_ingredients)
