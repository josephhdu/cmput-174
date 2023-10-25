from random import randint

def roll_die():
    return randint(1, 6)

def display_state():
    global xpos, opos
    lst = ['-', '-', '-', '-', '-', '-', '-', '-', ]
    lst[xpos] = 'x'
    lst[opos] = 'o'
    print("update: "+' '.join(lst))

def update_position(player, roll):
    global xpos, opos
    flag1, flag2 = False, False
    if player == 'x':
        if xpos+roll > 7:
            flag1 = True
        else:
            xpos += roll
        if xpos == opos:
            flag2 = True
            opos = 0
    else:
        if opos+roll > 7:
            flag1 = True
        else:
            opos += roll
        if xpos == opos:
            flag2 = True
            xpos = 0
    return (flag1, flag2)

def check_game_over():
    global xpos, opos
    if xpos == 7:
        return True
    elif opos == 7:
        return True
    else:
        return False

def opponent(player):
    if player == 'x':
        return 'o'
    else:
        return 'x'

def main():
    global xpos, opos
    print("Players begin in the starting position")
    print('*'*36)
    print("update: * - - - - - - -")
    print('*'*36)
    player = 'o'
    #Game Loop
    while True:
        player = opponent(player)
        input(f"Player {player} press enter to roll!")
        roll = roll_die()
        print(f"Player {player} rolled a {roll}")
        flag1, flag2 = update_position(player, roll)
        if flag1:
            print(f"The roll was too high, player {player} stays in this position")
        if flag2:
            print(f"{player} kicked the rival!")
        print('*'*36)
        display_state()
        print('*'*36)
        if check_game_over():
            print(f"Player {player} has won")
            break

if __name__ == '__main__':
    xpos, opos = 0, 0
    main()