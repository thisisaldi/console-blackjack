class Card:
    def __init__(self, rank: str, suit: str):
        self.rank: str = rank
        self.suit: str = suit
        if self.rank.isdigit():
            self.value: int = int(self.rank)
        elif self.rank == "A":
            self.value: int = 1
        else:
            self.value: int = 10
        if self.rank == "10":
            self.space = ''
        else:
            self.space = ' '
        
        suits_name = ['Spade', 'Diamond', 'Heart', 'Club']
        suits_symbols = ['♠', '♦', '♥', '♣']
        
        idx = suits_name.index(self.suit)
        self.symbol = suits_symbols[idx]
        
        self.layers = (
            '┌─────────┐',
            f'│{self.rank}{self.space}       │',
            f'│{self.symbol}        │',
            f'│    {self.symbol}    │',
            f'│        {self.symbol}│',
            f'│       {self.space}{self.rank}│',
            '└─────────┘'
        )
            
    def __str__(self):
        return f'{self.rank} of {self.suit}'
    