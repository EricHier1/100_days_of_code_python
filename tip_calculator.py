bill = input("How much is the bill?")
tip = input("What is the percent of the tip (5, 10, 15, 20, ect.)?")
tip_percent = float(tip) / 100
persons = input("How many people are splitting the bill?")

cost_per_person = (float(bill) / float(persons)) * ((1 + tip_percent))

rounded_cost_person = round(cost_per_person,2)

print(f"Each person should pay ${rounded_cost_person}")
