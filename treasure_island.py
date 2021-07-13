print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Eric's Treasure Island.")
print("Your mission is to find the treasure.")

choice_1 = input("You are walking towards the shore of the mainland and come to a fork in the road. " + "Do you go 'left' or 'right'?\n")

if choice_1 == "left" or choice_1 == "Left":
  choice_2 = input("You arrive in town and walk to the harbor. " + "Do you 'wait' or 'swim' to the island across the water?\n")
  if choice_2 == "wait" or choice_2 == "Wait":
    choice_3 = input("You wait for a boat and sail across the water." + "You see a 'red', 'blue', and 'green' door, which one do you choose.\n")
    if choice_3 == "red" or choice_3 == "Red" or choice_3 == "RED":
     print("You burst into flames as the dragon breathes fire though the now open door, GAME OVER.")
    elif choice_3 == "green" or choice_3 == "Green":
      print("You fall into a swamp and are eaten by the swamp montser, GAME OVER. ")
    elif choice_3 == "blue" or choice_3 == "Blue":
      print("You walk into a hall of wonders surrounded by treasure of all kinds, YOU WIN! ")
    else:
      print("Wrong choice, GAME OVER.")  
  else: 
    print("You try to swim across the water and are eaten by the Kraken, GAME OVER")
else: 
  print("You fall into a hole and die, GAME OVER")
  

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
