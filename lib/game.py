import ipdb
from board import Board
from column import Column
from move import Move
from player import Player


if __name__ == '__main__':

    backgammon = Board()
    player1 = Player('racquel')

    move1 = Move(backgammon, player1)
    move1.user_move()

    # move_1_start = input('Which column would you like to move from? ')


ipdb.set_trace()
    

    