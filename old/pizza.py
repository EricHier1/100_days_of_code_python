# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = int(0)
small_pizza = int(15)
medium_pizza = int(20)
large_pizza = int(25)

s_pep = int(2)
m_l_pep = int(3)

ex_cheese = int(1)

if size == "S":
  bill = small_pizza
  if add_pepperoni == "Y":
    bill += s_pep
  if extra_cheese == "Y":
    bill += ex_cheese

elif size == "M":
  bill = medium_pizza
  if add_pepperoni == "Y":
    bill += m_l_pep
  if extra_cheese == "Y":
    bill += ex_cheese

elif size == "L":
  bill = large_pizza
  if add_pepperoni == "Y":
    bill += m_l_pep
  if extra_cheese == "Y":
    bill += ex_cheese

print(f"Your final bill is ${bill}.")
