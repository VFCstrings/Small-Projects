from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffees = Menu()
coffee_machine=CoffeeMaker()
items = coffees.get_items()
money_process=MoneyMachine()

order_name = input(print(f"Please choose one of the following {items}."))

if order_name=="espresso" or order_name=="latte" or order_name=="cappuccino":
#Resources item selected
#look for the price of the object (item) in the original method __int__
	menuitem_item = coffees.find_drink(order_name)
	cost_item = coffees.find_drink(order_name).cost
	while coffee_machine.is_resource_sufficient(menuitem_item):

		# Resources item selected

		print(f"The total is {coffees.find_drink(order_name).cost}$.")

		if money_process.make_payment(cost_item):
			coffee_machine.make_coffee(menuitem_item)
			order_name = input(print(f"Please choose one of the following {items}."))
			if order_name == "off":
				exit()
			elif order_name == "report":
				coffee_machine.report()
				order_name = input(print(f"Please choose one of the following {items}."))
				if order_name=="espresso" or order_name=="latte" or order_name=="cappuccino":
					menuitem_item = coffees.find_drink(order_name)
					cost_item = coffees.find_drink(order_name).cost
			elif order_name == "espresso" or order_name == "latte" or order_name == "cappuccino":
				menuitem_item = coffees.find_drink(order_name)
				cost_item = coffees.find_drink(order_name).cost


if order_name=="off":
	exit()
if order_name=="report":
	coffee_machine.report()






