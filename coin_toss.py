# This is a game where two computers toss a coin to try an match the human player's call
# There are four games in a round and you can play multiple rounds

# Imports the random module used for the coin toss
import random

# Reads the textfile to print instructions
filename = 'instructions.txt'
filemode = 'r'
file = open(filename,filemode)
contents = file.read()
print(contents)
file.close()

# Assignments for the code
score_1 = 0
score_2 = 0    
tosses = 0
player1_toss = []
player2_toss = []
hh1 = 0
hh2 = 0
play_again = True
total_wins1 = 0
total_wins2 = 0
total_ties = 0

# While loop that allows the user to play multiple rounds
while play_again == True:

# While loop that computes the computer's flips and asks the users call
    while 4 > tosses:
        user_call = input('Heads or Tails ? Type H or T >') 
        options = ['H','T']
        computer_1 = random.choice(options)
        computer_2 = random.choice(options)
        print('Player 1 has tossed', computer_1)
        print('Player 2 has tossed', computer_2)
        player1_toss.append(computer_1)
        player2_toss.append(computer_2)

# If statments to compute which computer wins
        if user_call == computer_1 and user_call == computer_2:
            print('Player 1 wins')
            print('Player 2 wins')
            score_1 = score_1 + 1
            score_2 = score_2 + 1
        elif user_call == computer_1:
            print('Player 1 wins')
            score_1 = score_1 + 1
        elif user_call == computer_2:
            print('Player 2 wins')
            score_2 = score_2 + 1
    
        tosses = tosses + 1

# Resets the variables
    tosses = 0
    
# For statements that detect if there are H H pairs in the tosses
    for i in range(0,len(player1_toss)-1):
        first_value = player1_toss[i]
        second_value = player1_toss[i+1]
        if first_value == second_value and first_value == 'H' and second_value == 'H':
            hh1 += 1
    for i in range(0,len(player1_toss)-1):
        first_value2 = player2_toss[i]
        second_value2 = player2_toss[i+1]             
        if first_value2 == second_value2 and first_value2 == 'H' and second_value2 == 'H':
            hh2 += 1
            
# Prints the stats for the round
    print('ROUND STATS')
    if score_1 > score_2:
        total_wins1 += 1
        print('Player 1 wins this round')
    elif score_1 < score_2:
        print('Player 2 wins this round')
        total_wins2 += 1
    else:
        print('This round is a draw')
        total_ties += 1
            
    print('Player 1 points', score_1)
    print('Player 2 points', score_2)

# Prints the sequence of the the calls and shows the HH pairs
    print(player1_toss)
    print(player2_toss)
        
    print('H H found in the player 1 sequence',hh1,'times')
    print('H H found in the player 2 sequence',hh2,'times')

# Input for user to exit or play again
    user_playagain = input('Do you want to play another round? y/n>')
    if user_playagain == 'n':
        print("Thanks for playing")
        play_again = False
    else:
        play_again = True

# Resets the variables
    score_1 = 0
    score_2 = 0
    player1_toss = []
    player2_toss = []
    hh1 = 0
    hh2 = 0
    
# Prints the summary stats
print('SUMMARY STATS')
print('number of ties',total_ties)
print('number of player 1 wins',total_wins1)
print('number of player 2 wins',total_wins2)