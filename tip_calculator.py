print("Welcome to the tip calculator")
bill = input("How much is the bill? $")
tip = int(input("What is the percent of the tip(5, 10, 15, 20)? "))
tip_percent = float(tip) / 100
persons = int(input("How many people are splitting the bill?"))

cost_per_person = (float(bill) / float(persons)) * ((1 + tip_percent))

rounded_cost_person = "{:.2f}".format(round(cost_per_person,2))

print(f"Each person should pay ${rounded_cost_person}")
