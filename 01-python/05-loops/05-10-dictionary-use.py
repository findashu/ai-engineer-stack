# Using Dictionaries Instead of Repeated cases

users = [
    {"id":1, "total":100, "coupon":"p10"},
    {"id":2, "total":101, "coupon":"p17"},
    {"id":3, "total":140, "coupon":"p567"},
]

discounts = {
    "p10":(0.2,0),
    "p17":(0.7,4),
    "p567":(0.8,7),
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0,0))
    discount = user["total"] * percent + fixed
    print(f"{user["id"]} paid {user["total"]} and got discount for next visit of rupees {discount}")