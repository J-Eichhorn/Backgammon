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
    player2 = Player(player2_name.title(), 14)

    clear()

    backgammon = Board()

    while player1.score < 15 and player2.score < 15:
        move1 = Move(backgammon, player1)
        move1.user_move()
        if player1.score == 15:
            break
        else:
            move2 = Move(backgammon, player2)
            move2.user_move()
    print('game over')



ipdb.set_trace()
    

    