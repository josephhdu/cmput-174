import time
#for time.sleep command to pause between words
import os
#for os.system command to clear the screen between words

# to identify the terminals clear command
command = 'clear'
if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
   command = 'cls'
   os.system(command)

print('-'*50)
print('Remember the Word')
print('-'*50)

filename = "instructions.txt"
filemode = "r"  # read-only
file = open(filename, filemode)
contents = file.read()
file.close()
print(contents)

input("Press enter key to display the words")
os.system ('clear')

#input allows user to input something before showing more things

words = ['orange', 'chair', 'mouse', 'sandwitch']
for word in words:
   print(word)
   time.sleep(2)
   os.system('clear')


users_guess = input('What word begins with the letter c?')
if users_guess == 'chair':
   print('Congratulations, you are correct.')
else:
   print('Sorry, you entered', users_guess)
   print('The answer was chair.')

