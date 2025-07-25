from main import MENU, resources


def display_report():
    """displays the available resources of the coffee machine"""
    for item, amount in resources.items():
        print(f"{item} : {amount}")


def compare_with_resources(user_coffee):
    """compares the resources to make the user coffee with the available resources in machine"""
    user_coffee_ingredient = MENU[user_coffee]["ingredients"]
    if not user_coffee == "report":
        available_resources = list(resources.values())
        counter = 0

        # to prevent a logical error when the user wants an espresso
        if user_coffee == "espresso":
            available_resources.remove(available_resources[1])

        for ingredient, amount in user_coffee_ingredient.items():
            if amount > available_resources[counter]:
                print(f"Not enough {ingredient}")
                return False
            counter += 1
        return True

    else:
        return


def collect_money():
    """collects variaties of coins from the customer"""
    quarters = float(input("how many quarters? "))
    dimes = float(input("how many dimes? "))
    nickels = float(input("how many nickels? "))
    pennies = float(input("how many pennies? "))
    total_money_collected = round((quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01), 2)
    return total_money_collected


def validate_price(amount_paid, user_coffee):
    """checks if the amount paid by the user is sufficient to purchase the coffee"""
    change_amount = round(amount_paid - MENU[user_coffee]["cost"], 2)
    if amount_paid >= MENU[user_coffee]["cost"]:
        print(f"here is ${change_amount} in change")
        return True
    else:
        return False
    return


def make_coffee(user_coffee):
    user_coffee_ingredients = MENU[user_coffee]["ingredients"]
    resources["Money"] +=  MENU[user_coffee]["cost"]
    for ingredient, amount in user_coffee_ingredients.items():
        resources[ingredient] -= amount
    print(f"here is your {user_coffee}. Enjoy!")



# program flow
is_on = True
resources["Money"] = 0
while is_on:
    coffee_for_user = input("what would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_for_user == "off":
        break

    if not coffee_for_user == "report":
        # check if the coffee ordered has the available resources
        if compare_with_resources(coffee_for_user):
            # check if the money payed is enough to buy the coffee
            if validate_price(collect_money(), coffee_for_user):
                make_coffee(coffee_for_user)
            else:
                print(f"sorry you don't have enough money to buy a {coffee_for_user}")
    else:
        display_report()


    # return





















