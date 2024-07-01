from main import MENU, resources

water_available = resources["water"]
milk_available = resources["milk"]
coffee_available = resources["coffee"]


def money_coverter():
    print("Please insert coins.")
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    pennies = int(input("How many pennies?"))

    money = round((quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01), 2)
    return money


def compare(money, user_choice, water_available, milk_available, coffee_available):
    espresso_cost = MENU["espresso"]["cost"]
    latte_cost = MENU["latte"]["cost"]
    cappuccino_cost = MENU["cappuccino"]["cost"]

    espresso_count = MENU["espresso"]["ingredients"]
    latte_count = MENU["latte"]["ingredients"]
    cappuccino_count = MENU["cappuccino"]["ingredients"]

    if user_choice == "espresso":
        if espresso_count["water"] > water_available:
            print("Sorry there is not enough water")

        elif espresso_count["coffee"] > coffee_available:
            print("Sorry there is not enough coffee")

        else:
            if money >= espresso_cost:
                change = money - espresso_cost
                print(f"Here is ${change} in change")
                print(f"Here is your {user_choice}☕ Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")

    elif user_choice == "latte":
        if latte_count["water"] > water_available:
            print("Sorry there is not enough water")

        elif latte_count["milk"] > milk_available:
            print("Sorry there is not enough milk")

        elif latte_count["coffee"] > coffee_available:
            print("Sorry there is not enough coffee")

        else:
            if money >= latte_cost:
                change = money - latte_cost
                print(f"Here is ${change} in change")
                print(f"Here is your {user_choice}☕ Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")

    elif user_choice == "cappuccino":
        if cappuccino_count["water"] > water_available:
            print("Sorry there is not enough water")

        elif cappuccino_count["milk"] > milk_available:
            print("Sorry there is not enough milk")

        elif cappuccino_count["coffee"] > coffee_available:
            print("Sorry there is not enough coffee")

        else:
            if money >= cappuccino_cost:
                change = money - cappuccino_cost
                print(f"Here is ${change} in change")
                print(f"Here is your {user_choice}☕ Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")


def print_report(cost, water_available, milk_available, coffee_available):
    # print("Report---")
    print(f"Water : {water_available}ml")
    print(f"Milk : {milk_available}ml")
    print(f"Coffee : {coffee_available}g")
    print(f"Money : ${cost}")


cost = 0
need_to_next = True
while need_to_next:
    user_choice = input("What would you like? (espresso/latte/cappuccino):")
    if user_choice == "espresso":
        cost_espresso = MENU["espresso"]["cost"]
        cost += cost_espresso
        compare(money_coverter(), user_choice, water_available, milk_available, coffee_available)
        water_available -= MENU["espresso"]["ingredients"]["water"]
        coffee_available -= MENU["espresso"]["ingredients"]["coffee"]

    elif user_choice == "latte":
        cost_latte = MENU["latte"]["cost"]
        cost += cost_latte
        compare(money_coverter(), user_choice, water_available, milk_available, coffee_available)
        water_available -= MENU["latte"]["ingredients"]["water"]
        milk_available -= MENU["latte"]["ingredients"]["milk"]
        coffee_available -= MENU["latte"]["ingredients"]["coffee"]

    elif user_choice == "cappuccino":
        cost_cappuccino = MENU["cappuccino"]["cost"]
        cost += cost_cappuccino
        compare(money_coverter(), user_choice, water_available, milk_available, coffee_available)
        water_available -= MENU["cappuccino"]["ingredients"]["water"]
        milk_available -= MENU["cappuccino"]["ingredients"]["milk"]
        coffee_available -= MENU["cappuccino"]["ingredients"]["coffee"]

    else:
        print_report(cost, water_available, milk_available, coffee_available)





