# mutablity inside function
players = ["one","two","three"]

def update_player(team):
    team[1] = "four"

update_player(players) # argument
print(players)


def breakfast_order(item, bread, beverage):
    print(f"Breakfast order : {item, bread, beverage}")  

breakfast_order("Dosa", True , "tea") # positional args
breakfast_order(item = "Dosa", beverage = "tea", bread = False) # keyword args (kwargs)


def preparation(*items, **extras):
    print(f"Items: {items}") # returns tuple of args
    print(f"Items: {extras}") # returns Dictionary of kwargs

preparation("tomato","onion", spice = "medium", cheese = True)

# Default args

def allow_test(inp = True):
    print(f"Test allowed: {inp}")

allow_test();
allow_test(False);

# default traps

def update_list(results = []):
    results.append(100)
    print(results)

update_list() # [100]
update_list() # [100,100]
          
