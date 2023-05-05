# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

score_dig_1 = 0
score_dig_2 = 0

T = name1.lower().count("t")
R = name1.lower().count("r")
U = name1.lower().count("u")
E1 = name1.lower().count("e")

T += name2.lower().count("t")
R += name2.lower().count("r")
U += name2.lower().count("u")
E1 += name2.lower().count("e")

L = name1.lower().count("l")
O = name1.lower().count("o")
V = name1.lower().count("v")
E2 = name1.lower().count("e")

L += name2.lower().count("l")
O += name2.lower().count("o")
V += name2.lower().count("v")
E2 += name2.lower().count("e")

score_dig_1 += T + R + U + E1
score_dig_2 += L + O + V + E2

final_score = str(score_dig_1) + str(score_dig_2)
final_score_int = int(final_score)

# ?? how do i limit number to 0 to 100 range?
#?final_score.min() = 0
#?max(final_score) = 100

if final_score_int <= 10:
  print(f"Your score is {final_score_int}, you go together like coke and mentos.")
elif final_score_int >= 90:
  print(f"Your score is {final_score_int}, you go together like coke and mentos.")
elif final_score_int >= 40:
  print(f"Your score is {final_score_int}, you are alright toghether.")
elif final_score_int <= 50:
    print(f"Your score is {final_score_int}, you are alright toghether.")
else: 
  print(f"Your score is {final_score_int}.")
