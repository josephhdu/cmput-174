import random 

#Dictionary
#Make a full deck and shuffle
#make each card tuple wwith suit
#shuffle.random --> list
#list.pop[i] will remove and return
# have a rank list and for loop and assign based on index


class Card:
    
    def __init__(self, rank, suit): 
        self.rank = rank
        self.suit = suit
    
    def get_rank(self):
        return self.rank
      
    def display(self):
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
        
#        print(str(self.get_rank()) + ' of ' + self.suit)
        print(card + ' of ' + self.suit)
        
class Deck:
    
    def __init__(self):
        self.deck = []
        rank = [1,2,3,4,5,6,7,8,9,10,11,12,13] 
        suit = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        
        for i in rank:
            for j in suit:
                self.deck.append(Card(i, j))
        
    def shuffle(self):
        random.shuffle(self.deck)
        
#        for card in self.deck:
#            card.display()
        
        return self.deck
    
    def deal(self):
        topcard = self.deck.pop(0)
        
        return topcard       
        
#        print(value)
    
class Player:
    
    def __init__(self):
        self.player = []
    
    
    def add(self,card):
        self.player.append(card) 
    
    def ace_cards(self):
        aces = 0
        
        for card in self.player:
            if card.get_rank() == 1:
                aces += 1
        
        return aces        
        
    def display(self):
    
        for card in self.player:
            card.display()           
    
def main():
    
    game_continue = True
    
    while game_continue:
    
        deck = Deck()
        
        deck.shuffle()
        
        player_1 = Player()
        player_2 = Player() 
        
        for i in range(0,5):
            player_1.add(deck.deal())
            player_2.add(deck.deal())
    
        print('This is the hand of player 1:')
        player_1.display()
        
        print('This is the hand of player 2:')
        player_2.display()
 
        
        p1_aces = player_1.ace_cards()
        p2_aces = player_2.ace_cards()
        print('Number of ace cards in each players hand')
        print('player 1 has', p1_aces, 'aces')
        print('player 2 has', p2_aces, 'aces')
        
        print('Result:')
        
        if p1_aces > p2_aces:
            print('player 1 wins')
            game_continue = False
        elif p2_aces > p1_aces:
            print('player 2 wins')
            game_continue = False
        else:
            input('No winner, Press enter to shuffle again')
        
    
    

main()