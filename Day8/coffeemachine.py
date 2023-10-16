print(
    """   ___       __  __                   
  / __\___  / _|/ _| ___  ___         
 / /  / _ \| |_| |_ / _ \/ _ \        
/ /__| (_) |  _|  _|  __/  __/        
\____/\___/|_| |_|  \___|\___|        
                                      
                   _     _            
  /\/\   __ _  ___| |__ (_)_ __   ___ 
 /    \ / _` |/ __| '_ \| | '_ \ / _ \\
/ /\/\ \ (_| | (__| | | | | | | |  __/
\/    \/\__,_|\___|_| |_|_|_| |_|\___|
                                      """
)

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
    },
}


class COFFEE_MACHINE:
    def __init__(self):
        self.water = 300  # ml
        self.milk = 200  # ml
        self.coffee = 100  # g
        self.money = 0

    def confirmResources(self, order):
        for ingred, amount in MENU[order]["ingredients"].items():
            match ingred:
                case "water":
                    if amount > self.water:
                        return -1
                case "milk":
                    if amount > self.milk:
                        return -1
                case "coffee":
                    if amount > self.coffee:
                        return -1
                case _:
                    print("ERROR: Something happened with ingredient list")
                    exit(0)
        return 1

    def makeCoffee(self, order):
        for ingred, amount in MENU[order]["ingredients"].items():
            match ingred:
                case "water":
                    self.subWater(amount)
                case "milk":
                    self.subMilk(amount)
                case "coffee":
                    self.subCoffee(amount)
                case _:
                    print("ERROR: Something happened with ingredient list")
                    exit(0)
        self.printOrder(order)

    def printOrder(self, order):
        print(f"Thanks for ordering from Coffee Machine. Here's your {order} ☕")

    def subWater(self, amount):
        self.water -= amount

    def subMilk(self, amount):
        self.milk -= amount

    def subCoffee(self, amount):
        self.coffee -= amount

    def addBill(self, bill):
        self.money += bill

    def printReport(self):
        print(
            f"Water: {self.water}ml\nMilk: {self.milk}ml\nCoffee: {self.coffee}g\nMoney: ${'{:.2f}'.format(self.money)}"
        )


CM = COFFEE_MACHINE()  # Can also use initialization arguments

while True:
    user_input = input("What would you like? ( espresso | latte | cappuchino ): ")

    match user_input:
        case "espresso" | "latte" | "cappuchino":
            result = CM.confirmResources(user_input)
            if result == -1:
                print("Looks like we don't have enough ingredients for your order")
            else:
                # get user coins
                while True:
                    quarters = int(input("How many quarters?: "))
                    dimes = int(input("How many dimes?: "))
                    nickels = int(input("How many nickels?: "))
                    pennies = int(input("How many pennies?: "))
                    total = (
                        (quarters * 0.25)
                        + (dimes * 0.10)
                        + (nickels * 0.05)
                        + (pennies * 0.01)
                    )
                    if total >= MENU[user_input]["cost"]:
                        change = total - MENU[user_input]["cost"]
                        if change > 0:
                            print(f"Your change is: ${'{:.2f}'.format(change)}")
                        CM.addBill(MENU[user_input]["cost"])
                        break
                    else:
                        print(f"You didn't provide the right amount of money.")

                CM.makeCoffee(user_input)
        case "report":
            CM.printReport()
        case "off":
            print("Thanks!")
            break
        case _:
            print("Not valid input")
