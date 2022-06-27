from deck import Deck
from player import Player
from card import Card
import os

class Game:
    def __init__(self):
        self.deck: Deck = Deck()
        self.player1: Player = Player('Player 1')
        self.player2: Player = Player('Player 2')
        
        self.player1.draw_card(self.deck)
        self.player1.draw_card(self.deck)
        
        self.player2.draw_card(self.deck)
        self.player2.draw_card(self.deck)
        
        self.turn = 1
        self.gameover = False
        
    def player_turn(self):
        if self.check_stand():
            return None
        print(f'Player {self.turn}\'s Turn: ')
        print('1) Stand')
        print('2) Hit')
        
        self.choice = int(input('--> '))
        
        if self.choice == 1:
            if self.turn == 1:
                self.player1.stand = True
            elif self.turn == 2:
                self.player2.stand = True
        elif self.choice == 2:
            eval(f'self.player{self.turn}.draw_card(self.deck)')
        
        
        # Value more than 21
        if self.player1.value > 21:
            self.player2.win = True
        elif self.player2.value > 21:
            self.player1.win = True
            
    def check_stand(self):
        return (self.player1.stand and self.turn == 1) or (self.player2.stand and self.turn == 2)
    
    def check_gameover(self):
        if self.player1.value == 21:
            self.player1.win = True
        elif self.player2.value == 21:
            self.player2.win = True
        if self.player1.win or self.player2.win:
            return True
        if self.player1.stand and self.player2.stand:
            if self.player1.value > self.player2.value:
                self.player1.win = True
            elif self.player1.value < self.player2.value:
                self.player2.win = True
            else:
                self.player1.win = True
                self.player2.win = True
            return True

        return False
    
    def gameover_screen(self):
        os.system('cls')
        self.player1.show_hand()
        self.player2.show_hand()
        if self.player1.win and self.player2.win:
            print(f'DRAW!')
        elif self.player1.win:
            print(f'Player 1 WIN!')
        elif self.player2.win:
            print(f'Player 2 WIN!')

    def run(self):
        while not self.check_gameover():
            os.system('cls')
            self.player1.show_hand()
            self.player2.show_hand()
            self.player_turn()
            # Change Turn
            self.turn += 1
            if self.turn > 2:
                self.turn = 1
        
        self.gameover_screen()