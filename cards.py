# This code shuffles a deck of 52 cards of which two players draw 5 cards.
# The player who draws more ace cards is the winner
import random 

class Card:
    # Creates and object that represents a playing card
    def __init__(self, rank, suit): 
        # Initiates the rank and suit
        # - rank: a int value between 1-13
        # - suit: a string value to represent the suit
        self.rank = rank
        self.suit = suit
    
    def get_rank(self):
        # Return the int value of a card
        return self.rank
      
    def display(self):
        # Creates a string that represents a card
        card = ''
        if self.rank == 1:
            card = 'Ace'
        elif self.rank == 2:
            card = 'Two'
        elif self.rank == 3:
            card = 'Three'
        elif self.rank == 4:
            card = 'Four'
        elif self.rank == 5:
            card = 'Five'
        elif self.rank == 6:
            card = 'Six'
        elif self.rank == 7:
            card = 'Seven'
        elif self.rank == 8:
            card = 'Eight'
        elif self.rank == 9:
            card = 'Nine'
        elif self.rank == 10:
            card = 'Ten'
        elif self.rank == 11:
            card = 'Jack'
        elif self.rank == 12:
            card = 'Queen'
        elif self.rank == 13:
            card = 'King'       
        print(card + ' of ' + self.suit)
        
class Deck:
    # Creates and deck object that contains 52 cards
    def __init__(self):
        # Initiates the deck list and adds the 52 cards
        self.deck = []
        rank = [1,2,3,4,5,6,7,8,9,10,11,12,13] 
        suit = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        for i in rank:
            for j in suit:
                self.deck.append(Card(i, j))
        
    def shuffle(self):
        # Shuffles the deck
        random.shuffle(self.deck)
        return self.deck
    
    def deal(self):
        # Removes the top card
        topcard = self.deck.pop(0) 
        return topcard       

class Player:
    # Creates an object that holds 5 cards, representing a players hand
    def __init__(self):
        # Intiates the players hand
        self.player = []
    
    def add(self,card):
        # Adds 5 cards to the players hand
        self.player.append(card) 
    
    def ace_cards(self):
        # Checks for the number of ace cards in a players hand
        aces = 0
        for card in self.player:
            if card.get_rank() == 1:
                aces += 1
        return aces        
        
    def display(self):
        # Displays the players hand
        # - self is the 
        for card in self.player:
            card.display()           
    
def main():
    # main function
    
    # game loop
    game_continue = True
    while game_continue:
    
        # creates and shuffles the deck
        deck = Deck()
        deck.shuffle()
        
        # creates the players
        player_1 = Player()
        player_2 = Player() 
        
        # adds 5 cards into the deck
        for i in range(0,5):
            player_1.add(deck.deal())
            player_2.add(deck.deal())
    
        # prints the player's hands
        print('This is the hand of player 1:')
        player_1.display()
        print('') # To create space between the code
        print('This is the hand of player 2:')
        player_2.display()
        print('') # To create space between the code
        
        # prints the player's aces
        p1_aces = player_1.ace_cards()
        p2_aces = player_2.ace_cards()
        print('Number of ace cards in each players hand')
        print('Player 1 has', p1_aces, 'aces')
        print('Player 2 has', p2_aces, 'aces')
        print('') # To create space between the code
        
        # print the results and either ends or continues the game
        print('Result:')
        if p1_aces > p2_aces:
            print('Player 1 wins')
            game_continue = False
        elif p2_aces > p1_aces:
            print('Player 2 wins')
            game_continue = False
        else:
            input('No winner, press enter to shuffle again')

main()