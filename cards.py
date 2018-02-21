
from random import randint

class Card(object):
    """
    A class to deal with playcard objects
    """
    def __init__(self, card_suit, card_value):
        """
        A constructor to create a card with suit and value
        """
        self.suit = card_suit
        self.value = card_value
        
    def get_suit(self):
        # return the card suit
        return self.suit
    
    def get_value(self):
        # returns the card value
        return(self.value)
        
    def show(self):
        # display cards at the screen
        print("%s of %s" % (self.value,self.suit))

        
class Deck(object):
    """
    A class to deal with the deck of cards
    """
    
    def __init__(self):
        
        self.cards = [] # the cards array
        self.faces = [] # the array of faces
        self.royal = ["J","Q","K","A"] # faces of royal cards
        
        # let's build the deck
        self.build()
        
    def build(self):
        """
        The function builds a deck of cards
        """
        suits = ["Clubs","Hearts","Diamonds","Spades"]
        
        # first add cards with faces from 6 to 10
        self.faces = [str(num) for num in range(6,11)]

        # now add cards with royal faces
        for face in self.royal:
            self.faces.append(face)
        
        # build the deck of cards with different faces for four suits                
        self.cards = [Card(suit,face) for suit in suits for face in self.faces]
    
    def shuffle(self):
        """
        Shuffle the cards in the deck
        """
        for num in range(len(self.cards)-1,0,-1):
            # chose a random card in the deck
            new_num = randint(0,num)
            # swap two cards in the deck
            self.cards[num],self.cards[new_num] = self.cards[new_num],self.cards[num]
                
    def show(self):
        """
        The function shows all cards in the deck
        """
        for card in self.cards:
            card.show()
            
deck = Deck()
deck.shuffle()
deck.show()