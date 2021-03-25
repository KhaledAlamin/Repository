"""In this python file, I am trying to solve the problem
following mit 6.002 open courses where the objective is maximise the value
of a menu of foods"""


# I want to make a class to save any kind of food with its value in dollar 
# and its weight in calories
import random
class worker(object):
	def __init__(self, name, value, weight):
		self.name = name
		self.value = value
		self.weight	= weight
	def get_value(self):
		return self.value
	def get_weight(self):
		return self.weight
	def density(self):
		return self.value/self.weight
	def __add__(self, other):
		return self.object + other
	def __str__(self):
		return self.name + ": < " + str(self.value) + ', ' + str(self.weight)\
		+ ' >'

# next I want to build a menu from the food that I have

def build_menu(names, values, weights):
	menu = []
	for i in range(len(values)):
		menu.append(food(names[i], values[i], weights[i]))
	return menu


def building_large_menu(items, max_value, max_weight):
	foods = []
	for i in range(1, items):
		foods.append(food(str(i), random.randint(1, max_value),\
			random.randint(1, max_weight)))
	return foods	


# Now I have the menu what I want is to build optimization problem to choose 
# the maximum food in value given a constrain of weight in calories that
# I can not exceed
# Two algorithm will be used: Greedy and brute force
def greedy(items, max_weight, key):
	item_sort = sorted(items, key = key, reverse = True)
	tot_value, tot_weight = 0.0, 0.0
	result= []
	for i in range(len(item_sort)):
		if item_sort[i].get_weight() + tot_weight < max_weight:
			tot_weight += item_sort[i].get_weight()
			tot_value += item_sort[i].get_value()
			result.append(item_sort[i])
	return (result, tot_value)

def test_greedy(items, max_weight, key):
	res, value = greedy(items, max_weight, key)
	print('Total value of the food take are: ' + str(value))
	for item in res:
		print("		" + str(item))

def test_greedys(items, max_weight):
	print("Using greedy by value to assign " + str(max_weight) + ' calories')
	test_greedy(items, max_weight, food.get_value)
	print("Using greedy by weight to assign " + str(max_weight) + ' calories')
	test_greedy(items, max_weight, lambda x: 1/food.get_weight(x))
	print("Using greedy by density to assign " + str(max_weight) + ' calories')
	test_greedy(items, max_weight, food.density)


def max_value(items, max_weight, mem = {}):
	if (len(items), max_weight) in mem:
		result = mem[len(items), max_weight]
	elif items == [] or max_weight == 0:
		result = ((), 0)
	elif items[0].get_weight() > max_weight:
		result = max_value(items[1:], max_weight)
	else:
		next_item = items[0]
		to_take, to_take_value = max_value(items[1:], max_weight - next_item.get_weight())
		to_take_value += next_item.get_value()
		not_take, not_value = max_value(items[1:], max_weight)
		if to_take_value > not_value:
			result = (to_take + (next_item,), to_take_value)
		else:
			result = (not_take, not_value)
	mem[len(items), max_weight] = result
	return result

def test_maxValue(items, max_weight):
	result = max_value(items, max_weight)
	print('Using Brute force to assign ' + str(max_weight) + ' calories \
	 \nTotal value of the food taken are: ' + str(result[1]))
	for item in result[0]:
		print("		" + str(item))


names = ['wine', 'beer', 'pizza', 'burger', 'fries',
		'cola', 'apple', 'donut', 'cake']
values = [89, 90, 95, 100, 90, 79, 50, 10]

calories = [123, 154, 258, 354, 365, 150, 95, 195]

foods = build_menu(names, values, calories)
foods = building_large_menu(50, 300, 250)
test_greedys(foods, 900)
print()
test_maxValue(foods, 900)
