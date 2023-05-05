import random

# Define the ASCII art for each choice
ROCK = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

SCISSORS = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Store the choices in a dictionary
CHOICES = {
    "rock": ROCK,
    "paper": PAPER,
    "scissors": SCISSORS
}

# Define a function to print the ASCII art for a choice
def print_choice(choice):
    print(choice)

# Print a message to start the game
print("Let's play Rock-Paper-Scissors!")

# Start a while loop that keeps asking for the player's choice until they choose to quit
while True:
    # Ask the player for their choice
    player_choice = input("Enter your choice (rock/paper/scissors) or 'q' to quit: ").lower()

    # If the player chooses to quit, print a message and exit the loop
    if player_choice == "q":
        print("Thanks for playing!")
        break

    # If the player's choice is not one of the valid options, print an error message
    if player_choice not in CHOICES:
        print("Invalid choice!")
    else:
        # If the player's choice is valid, select a random choice for the computer
        computer_choice = random.choice(list(CHOICES.keys()))

        # Print the player's and computer's choices using the print_choice() function
        print("You chose:")
        print_choice(CHOICES[player_choice])
        print("Computer chose:")
        print_choice(CHOICES[computer_choice])

        # Determine the winner and print the result
        if player_choice == "rock" and computer_choice == "scissors":
            print("You win!")
        elif player_choice == "scissors" and computer_choice == "paper":
            print("You win!")
        elif player_choice == "paper" and computer_choice == "rock":
            print("You win!")
        elif player_choice == computer_choice:
            print("It's a tie!")
        else:
            print("You lose!")

