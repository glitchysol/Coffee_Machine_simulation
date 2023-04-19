from menu import MENU, resources
shut_down = False

valid_input = ["espresso", "latte", "cappuccino", "off", "report"]


def make_coffee():

    # TODO: 1. Prompt user by asking "what would you like? (espresso/latte/cappuccino):"
    while not shut_down:
        drink_selection = input("1. espresso\n2. latte\n3. cappuccino\nWhat would you like? ")
        if drink_selection == "1":
            drink_selection = "espresso"
        elif drink_selection == "2":
            drink_selection = "latte"
        elif drink_selection == "3":
            drink_selection = "cappuccino"

        # TODO: 2. Turn off the Coffee Machine by entering "off" to the prompt. (off = end of program)
        elif drink_selection == "off":
            return shut_down
            # break

        # TODO: 3. Print report (when prompted show current resource values)
        elif drink_selection == "report":
            for item in resources:
                print(item.capitalize(), ":", resources[item])
            print("\n")
            make_coffee()
        else:
            print("Try again.")
            make_coffee()
        # TODO: 4 Check resources sufficient?

        def enough_resources():
            if drink_selection == "espresso" or "latte" or "cappuccino":

                enough_water = True
                enough_coffee = True
                enough_milk = True

                if resources["water"] > MENU[drink_selection]["ingredients"]["water"]:
                    enough_water = True
                elif resources["water"] < MENU[drink_selection]["ingredients"]["water"]:
                    enough_water = False
                if resources["milk"] > MENU[drink_selection]["ingredients"]["milk"]:
                    enough_milk = True
                elif resources["milk"] < MENU[drink_selection]["ingredients"]["milk"]:
                    enough_milk = False
                if resources["coffee"] > MENU[drink_selection]["ingredients"]["coffee"]:
                    enough_coffee = True
                elif resources["coffee"] < MENU[drink_selection]["ingredients"]["coffee"]:
                    enough_coffee = False

                if not enough_coffee:
                    print("Sorry there is not enough coffee.\n")
                    return False
                elif not enough_milk:
                    print("Sorry there is not enough milk.\n")
                    return False
                elif not enough_water:
                    print("Sorry there is not enough water.\n")
                    return False
                elif enough_coffee and enough_milk and enough_water:
                    return True
            else:
                return shut_down

        # TODO: 5. Process coins

        if drink_selection == "cappuccino" or "latte" or "espresso":
            if enough_resources():

                print("Please insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickels = int(input("How many nickels?: "))
                pennies = int(input("How many pennies?: "))
                dollars = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)

            # TODO: 6. Check transaction successful

                if dollars > MENU[drink_selection]["cost"]:
                    change = dollars - MENU[drink_selection]["cost"]
                    print(f"Here is ${round(change, 2)} in change.")

                    # TODO: 7. Make Coffee and update resources

                    print(f"Here is your {drink_selection}. Enjoy!\n")
                    resources["money"] += (dollars - change)
                    resources["water"] -= MENU[drink_selection]["ingredients"]["water"]
                    resources["milk"] -= MENU[drink_selection]["ingredients"]["milk"]
                    resources["coffee"] -= MENU[drink_selection]["ingredients"]["coffee"]

                elif dollars < MENU[drink_selection]["cost"]:
                    print("Sorry that's not enough money. Money refunded.\n")
                    make_coffee()
        # TODO: 8. If not enough resources prompt user to order again

        # elif not enough_resources():

        elif drink_selection == "off":
            break

        else:
            make_coffee()


make_coffee()

# Had trouble getting the "off" action to work properly
