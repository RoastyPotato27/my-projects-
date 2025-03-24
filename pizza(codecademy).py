
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", 'anchovies', 'mushrooms']

prices = [2,6,1,3,2,7,2]

num_pizzas= len(toppings)

print("We sell " + str(num_pizzas) + " different kind of pizzas!")

pizza_and_prices = [[2,'pepperoni'], [6,'pineapple'], [1,'cheese'], [3,'sausage'], [2,'olives'], [7,'anchovies'],[2,'mushrooms']]
print()

pizza_and_prices.sort()
print()

cheapest_pizza = pizza_and_prices[0]

priciest_pizza = pizza_and_prices[6]

pizza_and_prices.pop(6)

pizza_and_prices.insert(4,[2.5, 'peppers'])
print(pizza_and_prices)
print()

three_cheapest = pizza_and_prices[:3]
print('three cheapest pizzas: ', three_cheapest)

print(priciest_pizza)
