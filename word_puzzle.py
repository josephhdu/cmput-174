# This program is a word guessing game.

# Imports the module random for choosing the word
import random

# This function reads and prints the intruction text
def instructions():
    filename = 'wp_instructions.txt'
    filemode = 'r'
    file = open(filename,filemode)
    contents = file.read()
    file.close
    print(contents)

# This function chooses the word that will be guessed by the user
def word_choice():
    words = ["apple","banana","watermelon","kiwi","pineapple","mango"]
    chosen_word = random.choice(words)
    return chosen_word

# This is the function does all computing for the game
def guess(chosen_word):

# Assignments 
    spaces = len(chosen_word)
    space_list = list('_'*spaces)
    word_list = list(chosen_word)
    
# The amount of wrong guesses the user can have
    turns = 4
    
    while turns > 0:

# Shows the guesses remaining and asks for users guess
        print('(',turns,'guesses remaining )')
        guess = str(input('Guess a letter:')) 

# Swaps out the guessed letter into the puzzle state
        if guess in chosen_word:
            for i in range(len(chosen_word)):
                if guess == chosen_word[i]:
                    space_list[i] = guess

                 
            print('The answer so far is',*space_list)

# Adds to guess counter if answer doesn't match
        else:
            print('The answer so far is',*space_list)
            turns -= 1

# Win condition code
        if word_list == space_list:
            print('Good job, you found the word',chosen_word)
            input('Press enter to end the game')
            break # Ends the loops if user wins

# Lose condition code
    else:
        print('Not quite, the answer was',chosen_word,'Better luck next time')
        input('Press enter to end the game')

# Main function combines all of the other functions
def main():
    instructions()
    chosen_word = word_choice()
    guess(chosen_word)
    
main()