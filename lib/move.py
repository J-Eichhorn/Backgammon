import random

class Move:

    def __init__(self, board, player):
        self.board = board
        self.player = player

        self.dice = []
        self.roll_dice()

    def roll_dice(self):
        self.dice.append(random.randint(1,6))
        self.dice.append(random.randint(1,6))
        print(f'You rolled: {self.dice[0]} and {self.dice[1]}')

    def user_move(self):
        valid_origin = False
        valid_destination = False
        
        origin_column = input('Which column would you like to move from? ')
        while valid_origin == False:
            if self.board.columns[int(origin_column) - 1].color_status == self.player.color:
                valid_origin = True
            else:
                origin_column = input('Please enter valid column: ')
        destination_column = input('Which column would you like to move to? ')

        if int(destination_column) - int(origin_column) > 0:
            check_direction = 'up'
        else:
            check_direction = 'down'

        while valid_destination == False:
            if (self.board.columns[int(destination_column) - 1].color_status == self.player.color or None) and self.player.direction == check_direction:
                #num_pieces maneuvering
                self.board.columns[int(origin_column) - 1].num_pieces -= 1
                if self.board.columns[int(origin_column) - 1].num_pieces == 0:
                    self.board.columns[int(origin_column) - 1].color_status = None
                self.board.columns[int(destination_column) - 1].num_pieces += 1
                self.board.columns[int(destination_column) - 1].color_status == self.player.color
                for i in range(24):
                    self.board.columns[i].set_occupied()
                valid_destination = True
            elif self.board.columns[int(destination_column) - 1].color_status != self.player.color and self.board.columns[int(destination_column) - 1].occupied == False and self.player.direction == check_direction:
                #num_pieces maneuvering
                self.board.columns[int(origin_column) - 1].num_pieces -= 1
                self.board.columns[int(destination_column) - 1].color_status == self.player.color
                for i in range(24):
                    self.board.columns[i].set_occupied()
                valid_destination = True
                #jail behavior
            else:
                destination_column = input('Please enter valid column: ')

        # self.board.create_board()


    
    


