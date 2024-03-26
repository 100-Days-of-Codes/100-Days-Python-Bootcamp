print("Welcome to the tip calculator.")

total_bill = input("What was the total bill? $")

tip_percent = input("What percentage tip would you like to give? 10, 12, or 15? %")

people_len = input("How many people to split the bill? ")

pay_amount = (float(total_bill) * (1 + int(tip_percent)/100)) / int(people_len)

print(f"Each person should pay: ${round(pay_amount, 2)}")