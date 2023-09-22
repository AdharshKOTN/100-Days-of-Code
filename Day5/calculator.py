print(
    """ _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|"""
)
print(
    """_______ _______        _______ _     _        _______ _______  _____   ______
 |       |_____| |      |       |     | |      |_____|    |    |     | |_____/
 |_____  |     | |_____ |_____  |_____| |_____ |     |    |    |_____| |    \_"""
)


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def div(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("Cannot divide by 0")


running_total = 0

fresh = "2"

while True:
    if fresh == "2":
        running_total = 0
        num1 = int(input("What's the first number?: "))
    else:
        num1 = running_total
    oper = str(input("+\n-\n*\n/\nPick an operation: "))
    num2 = int(input("Whats the next number?: "))

    output = 0

    match oper:
        case "+":
            output = add(num1, num2)
        case "-":
            output = sub(num1, num2)
        case "*":
            output = mult(num1, num2)
        case "/":
            output = div(num1, num2)
        case _:
            print("Not a valid operand")
            continue

    running_total = output

    print(f"{num1} {oper} {num2} = {output} ")

    fresh = str(
        input(
            f"Would you like to use this value in a running total or have a fresh calculation or exit? ( 1 or 2 or 3)"
        )
    )

    if fresh == "3":
        break
