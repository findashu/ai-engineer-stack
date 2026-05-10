menu_in_inr = {
    "dosa":65,
    "idli":20,
    "tea":12,
    "coffee":12,
    "vada":20,
}

menu_in_usd = {item:price/90 for item,price in menu_in_inr.items()}
print(menu_in_usd)