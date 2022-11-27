import random
from random import randint

border = '-'* 80
class Card:
    #initializes the two parameters for each attribute.
    def __init__(self, suit, rank):
        self.suit = suit #these are called instance attributes
        self.rank = rank
        
    suit_names = ['Clubs','Diamonds','Hearts','Spades']
    rank_names = [None,None,'2','3','4','5','6','7','8',
                  '9','10','Jack','Queen','King','Ace']
    
    #Including None ensures that index 0 and 1 will be None and
    #index 2 will be card number 2.
    
    '''variables like suit_names and rank_names which are defined
    inside a class but outside of any method are called
    class attributes because they are associated with the
    class object Card unlike the instance attributes above (suit, rank)'''
    
    def __str__(self):
        return '{} of {}'.format(Card.rank_names[self.rank],
                             Card.suit_names[self.suit])
    #creating a __str__ method of Card
    
    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2
    
'''__lt__ is a built-in operator that just stands for 'less than'.
__lt__ takes two parameters, self and other, and outputs
True if self is less than other.  This method uses tuples to
store the data.'''


#card1 = Card(randint(0,3),randint(2,14))
# Instantiates an object with random variables in the place
# of the arguments for a random selection.
#print(card1)

class Deck:
    
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit, rank)
                self.cards.append(card)
                
    '''A nested loop is the most efficient way to
    populate a 52-card deck.  Since there are 4 suits and
    14 ranks from 2 to ace, the nested loop will fill a deck
    of cards with a unique instance of every type.'''
    
    def __str__(self): # returns all of the numeric values to strings
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res) # prints every card on a new line
    
# The previous line will print every element in the list on a
# new line and then join that list together.

    def pop_card(self):
        return self.cards.pop()
    # cards.pop() removes the last element in a list
    
    def add_card(self, card):
        return self.cards.append(card)
    # cards.append(card) adds the card back to the deck
    
    def shuffle(self):
        return random.shuffle(self.cards)
    #random.shuffle() will just rearrange a list of elements
    
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())
            
    def deal_hands(self, num_hands, cards_per_hand):
        '''deal hands
        num_hands: int
        cards_per_hand: list'''
        hand_list = []
        for i in range(num_hands):
            h = Hand(input('Enter player name:'))
            self.move_cards(h, cards_per_hand)
            hand_list.append(h)
        return hand_list
        


class Hand(Deck):
    
    '''This class utilizes inheritance because the
    'child' class (Hand) is inheriting everything from the
    'parent' class (Deck) and being passed in as an argument.'''
    
    def __init__(self, label=''):
        self.cards = []
        self.label = label
        
    '''This initializer overwrites everything from the parent
    class so it becomes a blank slate that can use all of
    the parent class methods'''


# deck.shuffle() just rearranges the existing list, it does not create
# a new one, so storing deck.shuffle() in a new variable is pointless

d = Deck()
h = Hand(Deck)

def poker():
    deck = Deck()
    deck.shuffle()  
    for h in players:
        print(h.label)
        print(border,'\n')
        print(h,'\n')
    return players

poker()

