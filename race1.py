


import random

def roll_die():
    roll = random.randint(1,6)
    return roll

def display_state(game_state):
    print('*'*36)
    print('update:', *game_state)
    print('*'*36)

def update_position(roll,turn, game_state, x_position, o_position):
    
    if o_position == 0:
        game_state[0] = 'o'
    
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
            
            
# Kick function    
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
            
  
             
    return x_position, o_position
                

def check_game_over(game_state, game_continue):
        if game_state[7] == 'x':
            game_continue = False
            print('*'*36)
            print('update:', *game_state)
            print('*'*36)
            print('player x has won')
        elif game_state[7] == 'o':
            game_continue = False
            print('*'*36)
            print('update:', *game_state)
            print('*'*36)
            print('print o has won')
        return game_continue


def opponent(turn):
    if turn == 'x':
        turn = 'o'
    else:
        turn = 'x'
    return turn

def main():
    turn = 'x'
    game_state = ['*','-','-','-','-','-','-','-']
    x_position = 0
    o_position = 0 
    game_continue = True
    
    print('Players begin in the starting position')
    
    
    while game_continue == True:
        display_state(game_state)
        roll = roll_die()
        input('Player' + ' ' + turn + ' ' + 'press enter to roll')
        temp = update_position(roll,turn, game_state, x_position, o_position)
        x_position = temp[0]
        o_position = temp[1]        
        turn = opponent(turn)
        game_continue = check_game_over(game_state, game_continue)
     
    
main()