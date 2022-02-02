


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#


# ASK FOR USER INPUT


user_choice = input("Please choose one of: 'rock', 'paper', 'scissors' : ")

print("USER CHOSE:", user_choice)


# VALIDATIONS



# COMPUTER CHOICE
# https://docs.python.org/3/library/random.html#random.choice
# https://www.geeksforgeeks.org/python-select-random-value-from-a-list/
# https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/modules/random.md

#import random
from random import choice

options = ["rock", "paper", "scissors"]

#computer_choice = random.choice(options)
computer_choice = choice(options)

print("COMPUTER CHOSE: ", computer_choice)



# DETERMINE THE WINNER



# FINAL RESULTS
