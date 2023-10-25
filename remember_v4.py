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

header_boarder = print('-' * 70)
header_text = print('Remember The Word')

def header():
    os.system(clear_command)
    print(header_boarder)
    print(header_text)
    print(header_boarder)

def read_text(filename):
    filemode = "r"  # read-only
    file = open(filename, filemode)
    contents = file.read()
    file.close()
    return(contents)

def print_instruction():
    filename = "instructions.txt"
    shit = read_text(filename)
    print(shit)
    
def choose_word():
    filename = "words.txt"
    all_words_text = read_text_file(filename)
    all_words = all_words_text.splitlines()
    words = random.sample(all_words, k=4)
    return words

def show_words_list(words):
    input('Press enter to display the words')
    header()
    for word in words:
        print(word)
        time.sleep(2)
    header()
    
def provide_feedback(users_guess, correct_word):
    if users_guess == correct_word:
        print('Congratulations, you are correct.')
    else:
        print('Sorry, you entered', users_guess)
    print('The answer was', correct_word)

def main():
    play_again = True
    while play_again:
        print_instruction()
        header()
        words = choose_word()
        correct_word = word[0]
        random.shuffle(words)
        
        show_word_list(words)
        users_guess = input('What word begins with the letter ' + correct_word[0] + '?')
        provide_feedback(users_guess, correct_word)
        answer = input('Play again? y/n')
        if answer != y:
            play_again = false
            
main()
        