import random
from card import Card

class Deck:
    def __init__(self):
        ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
        suits = ('Heart', 'Diamond', 'Club', 'Spade')
        self.cards = []
        
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))
        
        random.shuffle(self.cards)
    
    def draw_card(self):
        return self.cards.pop(len(self.cards) - 1)
    
    def print_deck(self):
        for card in self.cards:
            print(card)
        