# This is a simple 2 player racing game.
# Each player rolls a 6-sided to move and you need to perfeclty move your piece
# into the last postion to win.

import random

def roll_die():
    # Rolls a die
    
    # Rolls a die and returns an int value used by other function
    roll = random.randint(1,6)
    return roll

def display_state(game_state):
    # Prints the current state of the game
    # game_state: is a list that stores the game state
    
    print('*'*36)
    print('update:', *game_state)
    print('*'*36)

def update_position(roll,turn, game_state, x_position, o_position):
    # Does the processing of the movement in the game
    # roll: int value that is the dice roll
    # turn: is either assigned to x or o to determine whos turn it is
    # game_state: is a list that stores the game state
    # x_position: int value that stores the position of x
    # o_position: int value that stores the position of o
    
    # For the inital part of the list to replace the *
    if o_position == 0:
        game_state[0] = 'o'
    
    # This if statement adds the dice rolls to assigned values for x and o
    # It also calculates if your roll was too high
    if turn == 'x':
        if x_position < 7:
            x_position = x_position + roll
            print('Player x rolled a', roll)
            if x_position > 7:
                x_position = x_position - roll
                print('The roll was too high, player', turn, 'stays in this position')
    elif turn == 'o':
        if o_position < 7:
            o_position = o_position + roll
            print('player o rolled a', roll)
            if o_position > 7:
                o_position = o_position - roll
                print('The roll was too high, player', turn, 'stays in this position')
    
    # This code moves the x or o along the track in the list
    if turn == 'x':
        for i in range(0, 7):
            if game_state[i] == "x":
                game_state[i] = "-"        
        for i in game_state:
            game_state[x_position] = 'x'
    elif turn == 'o':
        for i in range(0, 7):
            if game_state[i] == "o":
                game_state[i] = "-"
        for i in game_state:
            game_state[o_position] = 'o'
            
            
    # This code does all the computation for if kick happens   
    if x_position == o_position:
        print('player', turn, 'has kicked the rival')
        if turn == 'x':
            o_position = 0
            for i in range(0, 7):
                if game_state[i] == "o":
                    game_state[i] = "-"
            for i in game_state:
                game_state[o_position] = 'o'            
        else:
            x_position = 0
            for i in range(0, 7):
                if game_state[i] == "x":
                    game_state[i] = "-"        
            for i in game_state:
                game_state[x_position] = 'x'            
            
  
    # Returns the postion of x and o to be used by other functions
    return x_position, o_position
                

def check_game_over(game_state, game_continue):
    # Checks if the game is over
    # game_state: is a list that stores the game state
    # game_continue: either true for false, used for the main game loop 
    
    # Checks if the last position in the list is filled, if yes it ends the game
    # and prints the final positions.
    if game_state[7] == 'x':
        game_continue = False
        print('*'*36)
        print('update:', *game_state)
        print('*'*36)
        print('Player x has won!')
    elif game_state[7] == 'o':
        game_continue = False
        print('*'*36)
        print('update:', *game_state)
        print('*'*36)
        print('Player o has won!')
    
    # Returns that the game has ended
    return game_continue

def opponent(turn):
    # Swaps the turns between players
    # turn: is either assigned to x or o to determine whos turn it is
    if turn == 'x':
        turn = 'o'
    else:
        turn = 'x'
    return turn

def main():
    # This is the main function that contains the assignments and main game loop
    
    # Assignments
    turn = 'x'
    game_state = ['*','-','-','-','-','-','-','-']
    x_position = 0
    o_position = 0 
    game_continue = True
    
    # Prints the initial starting message
    print('Players begin in the starting position')
    
    # Main game loop
    while game_continue == True:
        display_state(game_state)
        roll = roll_die()
        input('Player' + ' ' + turn + ' ' + 'press enter to roll')
        positions = update_position(roll,turn, game_state, x_position, o_position)
        x_position = positions[0]
        o_position = positions[1]        
        turn = opponent(turn)
        game_continue = check_game_over(game_state, game_continue)
     
    
main()