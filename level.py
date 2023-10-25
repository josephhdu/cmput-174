# This code takes the score of two quizzes and puts you in a level
# There are three levels and level 3 being hard, 2 being medium, and 1 being easy
# You will be put in a higher level if you have higher scores

# Allows the user to input the marks for their quizzes
one = input('Enter the marks for quiz 1 > ')
two = input('Enter the marks for quiz 2 > ')

# Changes the string inputs into integers
one = int(one)
two = int(two)

# Varibles for numbers used in the compound statement below
high = 80
low = 50

# This compound statement does the processing of the user inputs and prints the results
if one>= high and two >= high:
    print('Level 3')
elif one >= low and two >= low:
    print('Level 2')
elif one >= low and two < low:
    print('Redo quiz 2')
elif two >= low and one < low:
    print('Redo quiz 1')
elif one < low and two < low:
    print('Level 1')
