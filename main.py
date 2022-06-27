from game import Game

if __name__ == '__main__':
    play = True
    while play:
        game = Game()
        game.run()
        if input('Play Again? (Y/Any)').lower() == 'y':
            play = True
        else:
            play = False