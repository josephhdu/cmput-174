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
    spaces = len(chosen_word)
    space_list = list('_'*spaces)
    word_list = list(chosen_word)
    live_list = []
    
#    guess = input('Guess a letter:')
    
    turns = 4
    guess = ''
    
    while turns > 0:
        guess = str(input('Guess a letter:'))
#        print(*space_list)
        failed = 0

        if guess in chosen_word:
  
                
            for i in range(len(chosen_word)):
                if guess == chosen_word[i]:
                    space_list[i] = guess
                else:
                    failed += 1
       
        if failed == 0:
            print('You Win')
            break
 
            print(*space_list)
    
        else:
            turns -= 1

    else:
        print('You Lost ;(')
        
            
            
#    print(space_list) 
        
        
def main():
    instructions()
    chosen_word = word_choice()
    guess(chosen_word)
    
#while guess_counter != 0:

main()