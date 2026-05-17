def brew(flavour):
   if flavour not in ["masala", "giner", "cardamom"]:
      # using python provided exception
      raise ValueError("Invalid flavour. Please choose from masala, giner, or cardamom.")
   print(f"Brewing {flavour} tea.")
   
#brew("lemon")

# Create Custom Exception

class InvalidFlavourError(Exception):
    pass

def brew_two(flavour):
   if flavour not in ["masala", "giner", "cardamom"]:
      # using custom exception
      raise InvalidFlavourError("Invalid flavour. Please choose from masala, giner, or cardamom.")
   print(f"Brewing {flavour} tea.")


brew_two("lemon")