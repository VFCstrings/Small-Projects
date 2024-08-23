from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffees = Menu()
coffee_machine=CoffeeMaker()
items = coffees.get_items()
money_process=MoneyMachine()

is_on=True

while is_on:
	order_name = input(print(f"Please choose one of the following {items}."))
	if order_name=="off":
		is_on=False
		exit()
	elif order_name=="report":
		coffee_machine.report()
		money_process.report()
	else:
	#Resources item selected
	#look for the price of the object (item) in the original method __int__
		menuitem_item = coffees.find_drink(order_name)
		cost_item = coffees.find_drink(order_name).cost
		if coffee_machine.is_resource_sufficient(menuitem_item):

			# Resources item selected

			print(f"The total is {coffees.find_drink(order_name).cost}$.")

			if money_process.make_payment(cost_item):
				coffee_machine.make_coffee(menuitem_item)








