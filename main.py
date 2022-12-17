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
}

money = 0
on=True
while on==True:
    choice=input("What would you like? (espresso/latte/cappuccino):")

    if choice=="off":
        break
    elif choice == "report":
        print(f"Water:{resources['water']}")
        print(f"Milk:{resources['milk']}")
        print(f"Coffee:{resources['coffee']}")
        print(f"Money:{money}")
        continue

    print("Please insert coins.")
    quarters=int(input("How many quarters?:"))
    dimes=int(input("How many dimes?:"))
    nickles=int(input("How many nickles?:"))
    pennies=int(input("How many pennies?:"))
    customer_cash=0.25*quarters+0.1*dimes+0.05*nickles+0.01*pennies





    if choice=="espresso":
        if customer_cash>=MENU["espresso"]["cost"]:
            profit=MENU["espresso"]["cost"]
            change=round(customer_cash-profit,2)


            if resources["water"]-MENU["espresso"]["ingredients"]["water"]>=0 and  resources["coffee"]-MENU["espresso"]["ingredients"]["coffee"]>=0:
                resources["water"]-=MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]

                money+=profit

            print(f"Here is ${change}.")
            print("Here is your espresso. Enjoy!")


        else:
            print("Sorry that's not enough money. Money refunded")

    elif choice=="latte":
        if customer_cash >= MENU["latte"]["cost"]:
            profit = MENU["latte"]["cost"]
            change = round(customer_cash-profit,2)


            if resources["water"]-MENU["latte"]["ingredients"]["water"]>=0 and  resources["coffee"]-MENU["latte"]["ingredients"]["coffee"]>=0 and resources["milk"]-MENU["latte"]["ingredients"]["milk"]>=0:
                resources["water"]-=MENU["latte"]["ingredients"]["water"]
                resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                money += profit
            else:
                print("Sorry there's not enough ")


            print(f"Here is ${change}.")
            print("Here is your latte. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded")



    elif choice=="cappuccino":
        if customer_cash >= MENU["cappuccino"]["cost"]:
            profit = MENU["cappuccino"]["cost"]
            change = round(customer_cash-profit,2)


            if resources["water"]-MENU["cappuccino"]["ingredients"]["water"]>=0 and  resources["coffee"]-MENU["cappuccino"]["ingredients"]["coffee"]>=0 and resources["milk"]-MENU["cappuccino"]["ingredients"]["milk"]>=0:
                resources["water"]-=MENU["cappuccino"]["ingredients"]["water"]
                resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                money += profit

            print(f"Here is ${change}.")
            print("Here is your cappuccino. Enjoy!")

        else:
            print("Sorry that's not enough money. Money refunded")




















