import ipdb
from board import Board
from column import Column
from move import Move
from player import Player


if __name__ == '__main__':

    
    
    player1 = Player('racquel')
    player2 = Player('josh')

    backgammon = Board()

    for i in range(3):
        move1 = Move(backgammon, player1)
        move2 = Move(backgammon, player2)
        move1.user_move()
        move2.user_move()

    # move_1_start = input('Which column would you like to move from? ')


ipdb.set_trace()
    

    