# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

current_days = int(age) * 365
current_weeks = int(current_days) / 7
current_months = int(age) * 12

#Change 1st number to how long you think you will live (defaults to 100)
life_days = 100 * 365
life_months = 100 * 12
life_weeks = 100 * 52

days_remain = (int(life_days) - int(current_days))
weeks_remain = (int(life_weeks) - int(current_weeks))
months_remain = (int(life_months) - int(current_months))

print(f"You have {days_remain} days, {weeks_remain} weeks, {months_remain} months left")
