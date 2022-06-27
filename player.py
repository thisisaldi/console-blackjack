from deck import Deck
from card import Card

class Player:
    def __init__(self, name: str):
        self.name: str = name
        self.value: str = 0
        self.hand = []
        self.stand = False
        self.win = False
        
    def draw_card(self, deck: Deck):
        card: Card = deck.draw_card()
        self.hand.append(card)
        if card.rank == 'A' and self.value <= 10:
            self.value += 11
        else:
            self.value += card.value
    
    def show_hand(self):
        print(f'{self.name}: {self.value} points')
        for layer in range(7):
            for card in self.hand:
                print(card.layers[layer], end=' ')
            print()