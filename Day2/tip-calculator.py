print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percent = (int(input("What percentage tip would you like to give? 10, 12 or 15? ")) / 100 ) + 1
party_size = int(input("How many people split the bill? "))
individual_payment = total_bill * tip_percent / ( party_size if party_size > 1 else 1 )
print(f"Each person should pay: ${'{:.2f}'.format(individual_payment)}")