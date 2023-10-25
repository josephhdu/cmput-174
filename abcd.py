# CMPUT 174 Fall 2021 Section A6
# September 9
# "Remember the Word" game, version 2

import os
import time

# Identify our Terminal's clear command
# You may need to change this if your terminal has 
# a different command
clear_command = 'clear'
if os.name == 'nt':
    clear_command = 'cls'
os.system(clear_command)

print('-' * 70)
print('Remember The Word')
print('-' * 70)

filename = "instructions.txt"
filemode = "r"  # read-only
file = open(filename, filemode)
contents = file.read()
file.close()
print(contents)

input('Press enter key to display the words.')
os.system(clear_command)

words = ['orange', 'chair', 'mouse', 'sandwich']
for word in words:
    print(word)
    time.sleep(2)
    os.system(clear_command)

users_guess = input('What word begins with the letter c?')
if users_guess == 'chair':
    print('Congratulations, you are correct.')
else:
    print('Sorry, you entered', users_guess)
print('The answer was chair.')

answer = input('Play again (y/N)?')
if answer == 'y':
    print('OK, play again')