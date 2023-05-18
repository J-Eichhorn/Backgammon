import ipdb
from board import Board
from column import Column
from move import Move
from player import Player
import os


if __name__ == '__main__':

    
    def clear():

        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')
    
    clear()

    player1_name = input('Player 1 name: ')
    player1 = Player(player1_name.title())
    player2_name = input('Player 2 name: ')
    player2 = Player(player2_name.title())

    clear()

    # player1 = Player('racquel')
    # player2 = Player('joshua eichhorn')

    backgammon = Board()

    for i in range(3):
        move1 = Move(backgammon, player1)
        move2 = Move(backgammon, player2)
        move1.user_move()
        move2.user_move()



ipdb.set_trace()
    

    