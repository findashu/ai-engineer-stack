# Built-in Functions: Python interpretor has a number of functions and types built into it that are always available.


# function documentation string (has to be in very first line to be considered as doc in triple quotes)

def addition (a ,b=1):
    """
    Returns addition of 2 numbers
    """
    return a*b

def generate_bill (cup=0 ,bhajji=0):
    """
    Calculate the total bill
    :param cup: Number of chai cups
    : param bhajji: Number bhajji
    """
    return (cup*10) + (bhajji*5)

print(addition.__doc__)
print(addition.__name__)
print(generate_bill.__doc__)


#built-in

# help(len)