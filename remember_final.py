# CMPUT 174 Fall 2021 Section A6
# September 21
# "Remember the Word" game, version 4

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

# String constants for printing the header
header_border = '-' * 70
header_text = 'Remember The Word'

# User-defined function to clear screen and print the header
def print_header():
    os.system(clear_command)
    print(header_border)
    print(header_text)
    print(header_border)

# Read a text file and return a string with the contents
def read_text_file(filename):
    filemode = "r"  # read-only
    file = open(filename, filemode)
    contents = file.read()
    file.close()
    return contents

def print_instructions():
    filename = "instructions.txt"
    contents = read_text_file(filename)
    print(contents)

# Read list of words from file, select 4 randomly
def select_random_words():
    filename = "words.txt"
    all_words_text = read_text_file(filename)
    all_words = all_words_text.splitlines()
    words = random.sample(all_words, k=4)
    return words

#wait for the user to press 'enter'
#show 4 "random" words, each for a short time, and erase them again
def show_word_list(words):
    input('Press enter key to display the words.')
    print_header()
    for word in words:
        print(word)
        time.sleep(2)
        print_header()

#deal with user input
#print user message
def provide_feedback(users_guess, correct_word):
    if users_guess == correct_word:
        print('Congratulations, you are correct.')
    else:
        print('Sorry, you entered', users_guess)
    print('The answer was', correct_word)

# The main program. Calls other user-defined functions 
# to do most of the work.
def main():
    play_again = True
    while play_again:
        print_header()
        print_instructions()
        words = select_random_words()
        correct_word = words[0]
        random.shuffle(words) # makes sure the correct_word is 
                              # in a random order again
        show_word_list(words)
        users_guess = input('What word begins with the letter ' + correct_word[0] + '?')
        provide_feedback(users_guess, correct_word)
        answer = input('Play again (y/N)?')
        if answer != 'y':
            play_again = False
            
main()