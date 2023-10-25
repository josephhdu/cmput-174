# This is a dice program 

import random

number = input("How many die do you want to roll? ")
sides = input("How many sides on the die? ")

# process data
# while loop concept
sides = int(sides)
number = int(number)
dice_results = [ ]
dice_rolled = 0
while dice_rolled < number:
    result = random.randint(1,sides)
    dice_results.append(result)
    dice_rolled = dice_rolled + 1

# for loop concept
for fuck in dice_results:
    shit = shit + str(fuck) + " "
print (shit)
