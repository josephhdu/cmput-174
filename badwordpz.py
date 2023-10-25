
import random

def instructions():
    filename = 'wp_instructions.txt'
    filemode = 'r'
    file = open(filename,filemode)
    contents = file.read()
    file.close
    print(contents)
    
def word_choice():
    words = ["apple","banana","watermelon","kiwi","pineapple","mango"]
    chosen_word = random.choice(words)
    return chosen_word

def guess(chosen_word):
    guess_counter = 0 
    spaces = len(chosen_word)
    space_list = list('_'*spaces)
    check_list = list(0*spaces)
    word_list = list(chosen_word)
    live_list = []
    
    guess = input('Guess a letter:')
    
    for i in range(0, spaces):
        if guess == chosen_word[i]:
            live_list.append(i)
        print(live_list)
        
    
    
#    live_list = list('_'*spaces)
#    live_list = []

#while guess_counter < 4

    print('The answer so far is', *space_list)
#   guess = input('Guess a letter','(',4 - guess_counter,'guesses remaining)' )
    
    
    for letter in word_list:
        if guess == letter:
            for letter in space_list:
                
                
    return guess 
                
                
#                answer = letter.replace('_',letter)
#                live_list.append(answer)
#                print(live_list)

    
#        for letter in word_list:
#            if guess_1 == word_list:
#                print('right letter')
            
# make the '-' into a list
#        guess_counter += 1


def checker(): 
    live_list = []
    





def main():
    instructions()
    chosen_word = word_choice()
    guess(chosen_word)
    for i in range(0, len(chosen_word) - 1):
        if guess == chosen_word[i]:
            print("You got it bitch")
        else:
            print("retard")
main()