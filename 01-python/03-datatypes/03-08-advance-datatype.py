# Some advanced datatypes in Python include:    
#1. date and time (datetime module)
#2. calendar (calendar module)
#3. timedelta (datetime module)
#4. arrow (third-party library for date and time manipulation)
#5 collections (like namedtuple, defaultdict, Counter from collections module)
#6. numpy arrays (for numerical data)

# They just examples of some advanced datatypes, there are many more in Python and its libraries that can be used for various purposes. Will see in future lessons as we explore more libraries and their functionalities.

import arrow

brewing_time = arrow.utcnow()
print(f"Brewing time (UTC): {brewing_time}")

from collections import namedtuple
ChaiOrder = namedtuple('ChaiOrder', ['customer_name', 'chai_type', 'sugar_level'])
order1 = ChaiOrder(customer_name="John Doe", chai_type="Masala", sugar_level=5)
print(f"Chai order using namedtuple: {order1}")