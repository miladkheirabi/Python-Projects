from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money = MoneyMachine()
coffee_maker = CoffeeMaker()

# todo 1 --- making a while loop that only breaks on typing "off"
turn_off = 0
while turn_off != 1:
    # todo 2 --- asking "what would you like? (espresso/latte/cappuccino)"
    order = input(f"what would you like? {menu.get_items()} ").lower()
    if order == "off":
        turn_off = 1
    # todo 3 --- when a user enters "report" it should generate a report that shows the current resource values
    elif order == "report":
        coffee_maker.report()
        money.report()
    # todo 4 --- check if there are sufficient resources to make it. if not print f"sorry there is not enough {resource}"
    elif menu.find_drink(order) is not None:
        drink = menu.find_drink(order)
        # todo 5 --- if todo 4 was True then it should ask for coins.
        # todo 6 --- calculate the monetary value of the cons inserted. if it was too much it should offer change.
        # todo 7 --- check if money is enough. if not print "sorry that's not enough money. money refunded"
        if coffee_maker.is_resource_sufficient(drink):
            # todo 8 --- if todo 7 was True then it make coffe and take money as profit.
            if money.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)