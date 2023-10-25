# Two players roll a die which determines how far their icon moves, first to reach the last space wins
import random

def roll_die(current_player):
    # randomly chooses a number between one and six to be the player's roll
    # - current_player is type str and is used to display which player's roll it is
    input("Player " + current_player + " press enter to roll!")
    roll = random.randint(1,6)
    print("Player " + current_player + " rolled a " + str(roll))
    return roll

def create_track(track_filler, length, display_character):
    # creates the track that the game is played on
    # - track_filler is a str which is the sybol that each space on the track is filled with
    # - length is an int that determines how many spaces there will be on the track
    # - display_character is a str that is the symbol of when the players overlap at the start
    track = []
    track.append(display_character)
    for i in range(length - 1):
        track.append(track_filler)    
    return track

def display_state(track, display_character):
    # displays the current position of the icons on the track
    # - track is type list and is used to display the game state
    # - display character is a str which is the symbol that creates the border of the display
    print(display_character * 36)
    print("update: " + ' '.join(track))
    print(display_character * 36)
    
def update_position(current_player, player_position, roll, track, player):
    # updates the positions of the players based on the roll
    # - current_player is type str used to determine whcih player's position should be updated
    # - player_position is a list containing ints, index 0 represents the x position and index 1 represents the o position
    # - roll is type int and is added to the position of the player
    # - track is type list and is updated based on the new positions
    # - player is a list of the players x and o used to display and the correct symbol
    if current_player == player[0]:
        player_index = 0
    else:
        player_index = 1
    track[player_position[player_index]] = '-'
    if player_position[player_index] + roll <= len(track) - 1:
        player_position[player_index] += roll
    else: 
        print("The roll was too high, player " + current_player + " stays in this position")
    if player_position[0] == player_position[1]:
        print(current_player + " kicked the rival!")
        if current_player == player[0]:
            player_position[1] = 0
        else:
            player_position[0] = 0
    track[player_position[0]] = player[0]
    track[player_position[1]] = player[1]

def check_game_over(track, track_filler, display_character):
    # determines whether a player has reached the final space and if so, prints the winner
    # - track is the list that this function checks the state of
    # - track filler is type str and is the symbol that is present in the track and is used to determine a win
    # - display character is a str which is the symbol that creates the border of the display in the display_state function call
    if track[-1] != track_filler:
        display_state(track, display_character)
        print("Player " + track[-1] + " has won!")
    return track[-1] != track_filler

def opponent(current_player, player):
    # switches current_player
    # - current player is type str and is used to determine which player's turn it should be
    # - player is a list of the players x and o used to determine which is the current player
    if current_player == player[0]:
        current_player = player[1]
    else:
        current_player = player[0]
    return current_player
        

def main():
    # this is the main function of the program and contains the game loop
    
    # prints the opening message of the game
    print("Players begin in the starting position")
    
    # stores the player and player position in a lists in the order x, o
    player = ['hello', 'goodbye']
    player_position = [0, 0]    
    
    # sets the initial values for the game
    continue_game = True
    current_player = player[0]
    track_length = 8
    track_filler = '-'
    display_character = '*'
    
    # creates a track for the game to be played on
    track = create_track(track_filler, track_length, display_character)
    
    # main game loop
    while continue_game:
        # displays the current game state
        display_state(track, display_character)       
       
        # rolls the die and displays the outcome
        roll = roll_die(current_player)
        
        # updates the position of the icons on the track
        update_position(current_player, player_position, roll, track, player)
        
        # determine whether a player has won the game and if so prints that that player won
        continue_game = not check_game_over(track, track_filler, display_character)
        
        # swtiches the current_player
        current_player = opponent(current_player, player)
main()