# Remember the Word 

import time 

# This prints the intro section
print("----------------------------------------------------------")
print("Remember the Word")
print("----------------------------------------------------------")
# A shortcut that you could use to print the lines is print('-'*50)


input("Press enter key to display the words")
#input allows user to input something before showing more things
print("Thanks for playing")
time.sleep(2)
print("orange")
time.sleep(2)
print("chair")
time.sleep(2)
print("mouse")
time.sleep(2) 

user_guess = input("What word begins with the letter c?")
print(user_guess)
print("congratulations, you are correct")
print('sorry, you entered', user_guess)
print('the answer is chair')


