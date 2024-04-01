from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

on = True


while on:
    option_chosen = input(f"Select an option ({menu.get_items()}): ")
    option_chosen = menu.find_drink(option_chosen)
    coffee_maker.is_resource_sufficient(option_chosen)
    money_machine.make_payment(option_chosen.cost)
    coffee_maker.make_coffee(option_chosen)

    answer = input("Would you like to make another drink? (yes or no): ")
    if answer.lower() == "no":
        break
    elif answer.lower() == "yes":
        on = True

    answer = input("Would you like to see the report? (yes or no): ")
    if answer.lower() == "no":
        continue
    elif answer.lower() == "yes":
        coffee_maker.report()
