from art import logo
import sys
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
def coffee_machine():        
    print(logo)
    drink = input ("What would you like? (espresso/latte/cappuccino): ").lower()
    if drink == 'report':
        print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}gm \nMoney: ${resources['money']} ")
        coffee_machine()
    if drink == 'end':
        print("GoodBye!")
        sys.exit()
    current_drink = MENU[drink]
    
    result = are_resources_sufficient(current_drink)
    if result != 1:
        print(result)
        coffee_machine()

    print("Please insert coins.")

    currency_quarter = float(input("How many quarters?: "))
    currency_dime = float(input("how many dimes?: "))
    currency_nickles = float(input("how many nickles?: "))
    currency_penny = float(input("how many pennies?: "))
    total_money = round(currency_quarter * .25 + currency_dime * .10 + currency_nickles * .05 + currency_penny * .01 , 2)


    if total_money > current_drink["cost"]:
        change = round(total_money - float(current_drink["cost"]), 2)
        print(f"Here is your ${change} change back.")
        print(f"Here is your {drink} ☕️. Enjoy!")
        resources["money"] += current_drink["cost"]        
        coffee_machine()
    elif total_money < current_drink["cost"]:
        print("Sorry that's not enough money. Money refunded.")        
        coffee_machine()
def are_resources_sufficient(drink_dictionary):
    if resources["water"] < drink_dictionary["ingredients"]["water"]:
        return "​Sorry there is not enough water."
    elif resources["water"] > drink_dictionary["ingredients"]["water"]:
        resources["water"] -= drink_dictionary["ingredients"]["water"] 
        return 1   
    elif ("milk" in drink_dictionary["ingredients"]):
        if (resources["milk"] < drink_dictionary["ingredients"]["milk"]):
            return "Sorry there is not enough milk."
        elif (resources["milk"] > drink_dictionary["ingredients"]["milk"]):
            resources["milk"] -= drink_dictionary["ingredients"]["milk"]
            return 1
    elif resources["coffee"] < drink_dictionary["ingredients"]["coffee"]:
        return "Sorry there is not enough coffee."
    elif resources["coffee"] > drink_dictionary["ingredients"]["coffee"]:
        resources["coffee"] -= drink_dictionary["ingredients"]["coffee"]
        return 1

coffee_machine()

