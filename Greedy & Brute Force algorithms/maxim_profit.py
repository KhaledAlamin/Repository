# I want to make a class to save any kind of worker contain number of workers, worker's salary in dollar and the profit they may acquired to the hiring company
import random
class worker(object):
	def __init__(self, name, num, salary, profit):
		self.name = name
		self.num = num
		self.salary = salary
		self.profit = profit
	def get_num(self):
		return self.num
	def get_salary(self):
		return self.salary
	def get_profit(self):
		return self.profit
	def net_salary(self):
		return self.profit - self.salary
	def __add__(self, other):
		return self.object + other
	def __str__(self):
		return self.name + ": < " + str(self.num) + ', ' + str(self.salary)\
		+ ', ' + str(self.profit) + ' >'

# next I want to build a profile for every worker

def build_profile(names, nums, salaries, profits):
	profile = []
	for i in range(len(nums)):
		profile.append(worker(names[i],nums[i], salaries[i], profits[i]))
	return profile


def building_large_profile(workers, max_nums, max_salaries, max_profits):
	profile = []
	for i in range(1, workers):
		profile.append(worker(str(i), random.randint(1, max_nums), \
		random.randint(1, max_salaries), random.randint(1, max_profits)))
	return profile	


# Now I have the profiles what I want is to build an optimization problem to choose 
# the maximum profits given a constrain of a budget I can not exceed
# Two algorithm will be used: Greedy and brute force

# Greedy
def greedy(profile, budget, key):
	profile_sort = sorted(profile, key = key, reverse = True)
	tot_salary, tot_profit = 0.0, 0.0
	result= []
	for i in range(len(profile_sort)):
		if profile_sort[i].get_salary() + tot_salary < budget:
			tot_salary += profile_sort[i].get_salary()
			tot_profit += profile_sort[i].get_profit()
			result.append(profile_sort[i])
	return (result, tot_profit)

def test_greedy(profiles, budget, key):
	res, profit = greedy(profiles, budget, key)
	print('Total profits of the workers taken are: ' + str(profit))
	for profile in res:
		print("		" + str(profile))
# Apply greedy based on different feature to optimize (profit to get, net salary of the workers, or gross salary)
def test_greedys(profiles, budget):
	print("Using greedy by profit to assign workers with budget " + str(budget) + ' $')
	test_greedy(profiles, budget, worker.get_profit)
	print("Using greedy by net_salary to assign  workers with budget " + str(budget) + ' $')
	test_greedy(profiles, budget, lambda x: 1/worker.net_salary(x))
	print("Using greedy by salary to assign workers with budget " + str(budget) + ' $')
	test_greedy(profiles, budget, lambda x: 1/worker.get_salary(x))

# Brute Force
def max_value(profiles, budget, mem = {}):
	if (len(profiles), budget) in mem:
		result = mem[len(profiles), budget]
	elif profiles == [] or budget == 0:
		result = ((), 0)
	elif profiles[0].get_salary() > budget:
		result = max_value(profiles[1:], budget)
	else:
		next_item = profiles[0]
		to_take, to_take_value = max_value(profiles[1:], budget - next_item.get_salary())
		to_take_value += next_item.get_profit()
		not_take, not_value = max_value(profiles[1:], budget)
		if to_take_value > not_value:
			result = (to_take + (next_item,), to_take_value)
		else:
			result = (not_take, not_value)
	mem[len(profiles), budget] = result
	return result

def test_maxValue(profiles, budget):
	result = max_value(profiles, budget)
	print('Using Brute force to assign budget ' + str(budget) + ' $ \
	 \nTotal profits of the workers taken are: ' + str(result[1]))
	for profile in result[0]:
		print("		" + str(profile))


###	-------------- Testing ---------------#####

random.seed(42)

num_workers = [13, 17, 10, 121, 69, 13, 82, 59, 110, 4, 126, 42, 102, 64, 93]
salary = [1300, 9805, 2931, 14693, 14137, 2674, 10325, 8297, 10471, 918, 14193, 14137, 2674, 10325, 8297]
profit = [12000,10325,17716,50870,43702,7151,59544,29361,38447,12000,30000,43702,7151,59544,29361]
names = []
for i in range(len(num_workers)):
    names.append('worker' + str(i))

#workers = build_profile(names, num_workers, salary, profit)

workers = building_large_profile(50, 150, 10732, 6000)
test_greedys(workers, 15000)
print()
test_maxValue(workers, 15000)


'''						RESULTS

Using greedy by profit to assign workers with budget 15000 $
Total profits of the workers taken are: 33332.0
		15: < 68, 712, 5978 >
		27: < 44, 8752, 5974 >
		7: < 144, 3258, 5866 >
		46: < 142, 189, 5573 >
		20: < 18, 751, 5418 >
		17: < 97, 1292, 4523 >
Using greedy by net_salary to assign  workers with budget 15000 $
Total profits of the workers taken are: 18432.0
		24: < 94, 2665, 3033 >
		38: < 138, 4305, 4789 >
		37: < 36, 4041, 4599 >
		48: < 88, 1828, 2405 >
		33: < 69, 1085, 1729 >
		31: < 84, 917, 1877 >
Using greedy by salary to assign workers with budget 15000 $
Total profits of the workers taken are: 37482.0
		46: < 142, 189, 5573 >
		1: < 29, 410, 2254 >
		4: < 109, 521, 245 >
		15: < 68, 712, 5978 >
		20: < 18, 751, 5418 >
		31: < 84, 917, 1877 >
		33: < 69, 1085, 1729 >
		17: < 97, 1292, 4523 >
		13: < 27, 1520, 3113 >
		22: < 60, 1655, 3114 >
		42: < 13, 1797, 1253 >
		48: < 88, 1828, 2405 >

Using Brute force to assign budget 15000 $ 	 
Total profits of the workers taken are: 45410
		46: < 142, 189, 5573 >
		33: < 69, 1085, 1729 >
		31: < 84, 917, 1877 >
		22: < 60, 1655, 3114 >
		20: < 18, 751, 5418 >
		17: < 97, 1292, 4523 >
		15: < 68, 712, 5978 >
		13: < 27, 1520, 3113 >
		10: < 2, 2616, 5720 >
		7: < 144, 3258, 5866 >
		4: < 109, 521, 245 >
		1: < 29, 410, 2254 >

As seen the Brute force give the best profits for the problem with
Compelxity of time with O(nlogn) compared with the greedy algorthim

'''
