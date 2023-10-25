# This is a game called guess the number
# The user is prompted to enter a number between 1 and 10.
# After the program will show the user if they guessed the right number

# Imports the module that gives access to random fuctions
import random

# Instruction for the player
print('I am thinking of a number between 1 and 10')

# Generates the random number
number = random.randint(1,10)

# Allows the user to enter their guess of the number
user_answer = input('What is the number?: ')

# Shows the number and users guess
print('The number was', number)
print('You guessed', user_answer)
