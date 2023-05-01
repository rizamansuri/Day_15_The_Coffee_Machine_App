# *********** BismillahirRahmannirRahim *********** #
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def make_drink(drink):
    """Makes the drink and reduces the ingredients used from resources."""
    desired_drink = MENU[drink]["ingredients"]
    # print(f"Resources left before making {drink} are: {resources}")
    for ingredient in desired_drink:
        resources[ingredient] -= desired_drink[ingredient]
    # print(f"Resources left after making {drink} are: {resources}")


def is_coins_sufficient(drink):
    """Checks if the given money is sufficient to make the drink or not and then returns boolean value."""
    global profit
    q = 0.25
    d = 0.10
    n = 0.05
    p = 0.01
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total_amount = quarters*q + dimes*d + nickles*n + pennies*p
    # print(f"Your total amount is: {total_amount}")
    desired_drink_cost = MENU[drink]["cost"]
    # print(f"{drink} cost is: {desired_drink_cost}")
    if total_amount > desired_drink_cost:
        change = total_amount - desired_drink_cost
        change = round(change, 2)
        print(f"Here is ${change} in change.")
        profit += desired_drink_cost
    else:
        print(f"Sorry that's not enough money. Money refunded.")
        return False
    return True


def is_resources_sufficient(drink):
    """Checks whether there are sufficient resources available or not and returns boolean value."""
    is_sufficient = True
    desired_drink = MENU[drink]["ingredients"]
    for key in desired_drink:
        if resources[key] <= desired_drink[key]:
            print(f"Sorry there is not enough {key}.")
            is_sufficient = False
    return is_sufficient


def report():
    """Gives the report of available resources"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")



while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        exit(0)
    elif choice == "report":
        report()
    elif is_resources_sufficient(choice):
        if is_coins_sufficient(choice):
            make_drink(choice)
            print(f"Here is your {choice} ☕. Enjoy!")


