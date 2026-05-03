# You are building a ticket info system for railway app.
# Based on seat type, show features
# Task:
# Input: 'sleeper','AC','general','luxury'
# Match using match-case
# Unknown -> show: "Invalid seat type" 

seat_type = input("Enter seat type (sleeper, ac, general, luxury)").lower();

match seat_type:
    case "sleeper":
        print(f"Sleeper - No AC, beds available")
    case "ac":
        print(f"AC - Air conditioned, comfy ride")
    case "general":
        print(f"General - Cheapest option, No reservation")
    case "luxury":
        print(f"Luxury - Premium seats and meal")
    case _:
        print(f"Invalid seat type")