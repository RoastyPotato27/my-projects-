# Imports >
import datetime 
from decimal import Decimal 
from random import randint, choice
from Custom_module import *
# =============================================

# Cost of Time Travel >

base_cost = Decimal('1000.00')

current_year = datetime.datetime.now().year

# Input for target yyear >
target_year = randint(current_year,9999)

year_diff = target_year - current_year

# Cost >
cost_multiplier = Decimal(1 + 0.5 * year_diff)

total_cost = base_cost * cost_multiplier

# Destination >
places = ['Bali, Indonesia','New Orleans', 'Kerry, Ireland', 'Marrakesh, Morocco','Sydney', 'The Maldives', 'Paris, France', 'Cape Town, South Africa', 'Dubai, U.A.E.', 'New York']
destination = choice(places)



# Printing > 

print("Today's Date: ", datetime.date.today())
print('Current Time: ', datetime.datetime.now().time())
print(generate_time_travel_message(target_year,destination,total_cost))


