from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True
while is_on:
    option = menu.get_items()
    choice = input(f"What would you like? ({option}): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)



# is_on = True
# while is_on:
#     choice = input("What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#
#     elif choice == "report":
#         make_coffee.report()
#         money_operation.report()
#
#     else:
#         order = menu_operation.get_items()
#         drink = menu_operation.find_drink(choice)
#         if make_coffee.is_resource_sufficient(drink):
#             money_operation.process_coins()
#             make_coffee.make_coffee(drink)
#             menu_operation.menu

        # if is_resource_sufficient(drink['ingredients']):
        #     payment = process_coins()
        #     if is_transaction_successful(payment, drink['cost']):
        #         make_coffee(choice, drink['ingredients'])