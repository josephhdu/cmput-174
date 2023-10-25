#This program analyzes the the grades of university students

#Question 1
#first = 3
#second = 3 not needed shit

#first = input('What is the first grade: ')
#second = input('What is the second grade: ')

#int(first)
#int(second) not needed shit

#if first == second :
#    print(first, 'and', second, 'are equal')
#else:
#    print(first, 'and', second, 'are not equal')
    
    
#Question 2

#one = input('What is the first grade: ')
#two = input('What is the second grade: ')
#three = input('What is the third grade: ')

#if one > two and three:
#    print ('the highest grade is ', one)
#elif two > one and three:
#    print ('the highest grade is', two)
#else:
#    print ('the highest grade is', three)
    
#Question 3
#grade = input('Input the grade: ')
#shit = float(grade)

#if shit < 1:
#    print('The grade is a Failure!')
#elif 1 < shit < 1.3:
#    print('The grade is a Poor!')
#elif 1.3 < shit < 2.3:
#    print('The grade is Satisfactory!')
#elif 2.3 < shit < 3.3:
#    print('The grade is Good!')
#elif 3.3 < shit < 4.0:
#    print('The grade is Excellent!')
#else:
#    print('Invalid!')


#Question 4
one = input('Enter the marks for quiz 1 >: ')
two = input('Enter the marks for quiz 2 >: ')

fuck = int(one)
shit = int(two)

a = 80
b = 50

if fuck >= a and shit >= a:
    print('Level 3')
elif fuck >= b and shit >= b:
    print('Level 2')
elif fuck >= 50 and shit < 50:
    print('Redo quiz 2')
elif shit >= 50 and fuck < 50:
    print('Redo quiz 1')
elif fuck < 50 and shit < 50:
    print('Level 1')
