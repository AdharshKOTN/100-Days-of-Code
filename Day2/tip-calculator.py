print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percent = (float(input("What percentage tip would you like to give? 10, 12 or 15? ")) / 100 ) + 1
party_size = float(input("How many people split the bill? "))
individual_payment = round(total_bill * tip_percent / ( party_size if party_size > 1 else 1 ), 2)
print(f"Each person should pay: $" + str(individual_payment))