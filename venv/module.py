import  random

suits=('Hearts','Diamonds','Spades','Clubs')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Jack':10,'Queen':10,'King':10,'Ace':11}
playing=True

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank

    def __str__(self):
        return  self.rank + "of " +self.suit

class Deck:
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp=''
        for  card in self.deck:
            deck_comp+= '\n'+card.__str__()
        return  "The deck has:" + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
         single_card= self.deck.pop()
         return  single_card
class Hand:
    def __init__(self):
        self.cards=[]
        self.values=[]
        self.aces=[]

    def add_card(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]

    def adjust_for_ace(self):
         pass


test_deck= Deck()
print(test_deck)
test_player=Hand()
pulled_card=test_deck.deal()
test_player.add_card(pulled_card)
print(test_player.value)
test_player.add_card((test_deck.deal()))
test_player.value


