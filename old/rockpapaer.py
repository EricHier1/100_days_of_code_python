rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

choices = ["rock", "paper", "scissors"]
user_choice = input("Welcome to ROCK PAPER SCISSORS. Choose 'rock' 'paper' or 'scissors'\n").lower()
comp_choice = random.choice(choices)

#rock
if user_choice == "rock" and comp_choice == "scissors":
    print(f"[{rock}{scissors} Rock beats scissors, you win!")
elif user_choice == "rock" and comp_choice == "paper":
    print(f"[{rock}{paper} Paper beats rock, you lose!")
elif user_choice == "rock" and comp_choice == "rock":
    print(f"[{rock} {rock} Tie!")

#paper
if user_choice == "paper" and comp_choice == "scissors":
    print(f"[{paper}{scissors} Scissors beats paper, you lose!")
elif user_choice == "paper" and comp_choice == "paper":
    print(f"[{paper}{paper} Tie!")
elif user_choice == "paper" and comp_choice == "rock":
    print(f"[{paper} {rock} Paper beats rock, you win!")

#scissors
if user_choice == "scissors" and comp_choice == "scissors":
    print(f"[{scissors}{scissors} Tie!")
elif user_choice == "scissors" and comp_choice == "paper":
    print(f"[{scissors}{paper} Scissors beats paper, you win!")
elif user_choice == "scissors" and comp_choice == "rock":
    print(f"[{scissors} {rock} Rock beats scissors, you lose!")
else:
    print("Invalid choice, you lose!")
