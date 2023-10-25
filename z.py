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
    guesses = ''
    turns = 4

    while turns > 0:
        failed = 0
        for char in chosen_word:
            if char in guesses:
                print(char)
            else:
                print("_")
                failed += 1
        if failed == 0:
            print("You Win")
            print("The word is: ", chosen_word)
            break
        guess = input("guess a character:")
        guesses += guess
        if guess not in chosen_word:
            turns -= 1
            print("Wrong")
            print("You have", + turns, 'more guesses')
            if turns == 0:
                print("You Loose")
    
    
#    spaces = len(chosen_word)
#    space_list = list('_'*spaces)
#    check_list = list(0*spaces)
#    word_list = list(chosen_word)
#    live_list = []
    
#    guess = input('Guess a letter','(',guess_counter,'guesses remaining:')
    
#    print(guess)
    
#    guess_counter = 4
    

#    for i in range(0, spaces):
#        print(*space_list)
        
#        if guess == chosen_word[i]:
#            live_list.append(i)
#            space_list[i] = guess
        
#    if guess != chosen_word:
#        guess_counter += 1
            
            
#    print(space_list) 
        
        
def main():
    instructions()
    chosen_word = word_choice()
    guess(chosen_word)
    
#while guess_counter != 0:

main()