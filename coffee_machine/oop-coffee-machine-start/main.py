from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
make_coffee = CoffeeMaker()
input_money = MoneyMachine()

# menu_item = MenuItem(menu.find_drink(choice))
is_on = True
while is_on :
    options = menu.get_items()
    choice = input(f"Enter what you want {options} : ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        make_coffee.report()
        input_money.report()
    else:
        drink = menu.find_drink(choice)
        if input_money.make_payment(drink.cost):
            make_coffee.make_coffee(drink)


