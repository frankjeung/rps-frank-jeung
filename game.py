


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#

print("-------------------\n")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...\n")
print("-------------------\n")

# ASK FOR USER INPUT

user_choice = input("Please choose one of: 'rock', 'paper', 'scissors' : \n")
# https://www.freecodecamp.org/news/python-new-line-and-how-to-python-print-without-a-newline/
print("USER CHOSE:", user_choice, end='\n')


# VALIDATIONS

# https://www.w3schools.com/python/ref_string_lower.asp
user_choice.lower()

if user_choice == "rock" or user_choice == 'paper' or user_choice == 'scissors':
    pass
else:
    print("Invlaid Selection. Please choose one of: 'rock', 'paper', 'scissors'")
    exit()


# COMPUTER CHOICE

# https://docs.python.org/3/library/random.html#random.choice
# https://www.geeksforgeeks.org/python-select-random-value-from-a-list/
# https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/modules/random.md

#import random
from random import choice

options = ["rock", "paper", "scissors"]

#computer_choice = random.choice(options)
computer_choice = choice(options)

print("COMPUTER CHOSE:", computer_choice, end='\n')


# DETERMINE THE WINNER

print("-------------------\n")

if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("You won!")
    else:
        print("Oh, the computer won. It's ok.")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("You won!")
    else:
        print("Oh, the computer won. It's ok.")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("You won!")
    else:
        print("Oh, the computer won. It's ok.")


# FINAL RESULTS

print("-------------------\n")
print("Thanks for playing. Please play again!")