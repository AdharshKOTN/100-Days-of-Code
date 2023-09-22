from replit import clear

print(
    """___________
                         \         /
                          )_______(
                          |"""
    """"|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""
    """"(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\""""
)
more_bidders = True
user_dict = {}
while more_bidders:
    user_name = str(input("What is your name?: "))
    user_bid = float(input("How much are you bidding on the item?: $"))
    if user_name not in user_dict:
        user_dict[user_name] = user_bid
        more_users = str(input("Are there any more bidders?(Y/N): "))
        if more_users == "N":
            break
        clear()
    else:
        print("User already exists...")

# no more users added, go through dict and determine max
print(f"The winner of the bid is {max(user_dict)}")
