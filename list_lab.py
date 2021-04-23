#!/usr/bin/env python

#Below is all the series 1 functions
def series1():
	fruit_list = ['Apples','Pears','Oranges','Peaches']
	print(fruit_list)
	fruit_list.append(input("Add another fruit: "))
	print(fruit_list)
	ask_number = input("Give me a number and I will give you that number and fruit: ")
	index = int(ask_number) - 1
	print(f"The number is {ask_number}. The fruit is {fruit_list[index]}")
	add_fruit=[0]
	add_fruit[0] = input("Lets add another fruit: ")
	fruit_list = list(add_fruit) + list(fruit_list)
	print(fruit_list)
	add_fruit= input("Again, lets add another fruit: ")
	fruit_list.insert(0,add_fruit)
	print(fruit_list)
	print('Now lets display the list with just the fruits that begin with P')
	pfruit_list = []
	for fruit in fruit_list:
		if fruit.startswith('p') or fruit.startswith('P'):
			pfruit_list.append(fruit)
	print(pfruit_list)
	return fruit_list
pass

#Below is the start of series 2 functions
def series2(fruit_list):
	print("Let's display the fruit list again")
	print(fruit_list)
	print('We will now remove the last fruit from the list and redisplay it')
	fruit_list.pop(-1)
	print(fruit_list)
	ask_delete = input('Type in the fruit you want to see removed, this is case sensitive: ')
	fruit_list.remove(ask_delete)
	print(f'We have {ask_delete} removed the from the list, the new list is:')
	print(fruit_list)
pass

#Below is the start of series 3 functions
def series3(fruit_list):
	#First lets lowercase everything
	fruit_list = [fruit.lower() for fruit in fruit_list]
	liked_fruits=[] # need to create the list for liked fruits
	while len(fruit_list) > 0:#need a while loop to run
		response = input(f'Do you like {fruit_list[0]}, yes or no? ').lower()
		fruit = fruit_list[0]

		while response not in ['yes','y','n','no']:
			print("Please enter a 'yes' or 'no' response")
			response = input(f'Do you like {fruit_list[0]}, yes or no? ').lower()
			fruit = fruit_list[0]

		if response == 'n' or response == 'no':
			fruit_list.remove(fruit)

		if response == 'y' or response == 'yes':
			liked_fruits.append(fruit)
			fruit_list.remove(fruit)

	print(f'These are the fruits you like: {liked_fruits}')
pass

def series4(fruit_list):
	reversed_fruits=[] # need to create the list for liked fruits
	while len(fruit_list) > 0:#need a while loop to run
		fruit = (fruit_list[0])
		reversed_fruits.append(fruit[::-1])
		fruit_list.remove(fruit)

	print('Let us see those fruits spelt backwards...')
	print(reversed_fruits)
pass

series1_output = series1()
series2(series1_output)
series3(series1_output)
series4(series1_output)