# CMPUT 174 Fall 2021 Section A6
# September 14
# "Remember the Word" game, version 3

import os
import time
import random

# Identify our Terminal's clear command
# You may need to add another case with elif if your terminal has 
# a different command
if os.name == 'nt':
    clear_command = 'cls'
else:
    clear_command = 'clear'

print('-' * 70)
print('Remember The Word')
print('-' * 70)

filename = "instructions.txt"
filemode = "r"  # read-only
file = open(filename, filemode)
contents = file.read()
file.close()
print(contents)

filename = "words.txt"
filemode = "r"  # read-only
file = open(filename, filemode)
all_words_text = file.read()
file.close()
all_words = all_words_text.splitlines()
# print(all_words)
words = random.sample(all_words, k=4)
correct_word = words[0]
random.shuffle(words)

input('Press enter key to display the words.')
os.system(clear_command)

# words = ['orange', 'chair', 'mouse', 'sandwich']
for word in words:
    print(word)
    time.sleep(2)
    os.system(clear_command)

users_guess = input('What word begins with the letter ' + correct_word[0] + '?')
if users_guess == correct_word:
    print('Congratulations, you are correct.')
else:
    print('Sorry, you entered', users_guess)
print('The answer was', correct_word)

answer = input('Play again (y/N)?')
if answer == 'y':
    print('OK, play again')