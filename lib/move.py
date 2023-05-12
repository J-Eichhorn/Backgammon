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
        

    def user_move(self):
        
        for turn in range(2):

            if len(self.dice) == 2:
                print(f'You rolled: {*self.dice,}')
            else:
                print(f'Your remaining roll: ({self.dice[0]})')

            valid_origin = False
            valid_destination = False

            origin_column = input('Which column would you like to move from? ')
            while valid_origin == False:
                if self.board.columns[int(origin_column) - 1].color_status == self.player.color:
                    valid_origin = True
                else:
                    origin_column = input('Please enter valid column: ')
            destination_column = input('Which column would you like to move to? ')

            
            while valid_destination == False:
                
                if int(destination_column) - int(origin_column) > 0:
                    check_direction = 'up'
                else:
                    check_direction = 'down'

                if abs(int(destination_column) - int(origin_column)) in self.dice:

                    if (self.board.columns[int(destination_column) - 1].color_status == self.player.color or "None") and self.player.direction == check_direction:
                        
                        self.board.columns[int(destination_column) - 1].num_pieces += 1
                        self.board.columns[int(origin_column) - 1].num_pieces -= 1
                        if self.board.columns[int(origin_column) - 1].num_pieces == 0:
                            self.board.columns[int(origin_column) - 1].color_status = "None"
                        self.board.columns[int(destination_column) - 1].color_status = self.player.color
                        for i in range(24):
                            self.board.columns[i].set_occupied()
                        valid_destination = True

                    elif self.board.columns[int(destination_column) - 1].color_status != self.player.color and self.board.columns[int(destination_column) - 1].occupied == False and self.player.direction == check_direction:
                        
                        self.board.columns[int(origin_column) - 1].num_pieces -= 1
                        self.board.columns[int(destination_column) - 1].color_status = self.player.color
                        for i in range(24):
                            self.board.columns[i].set_occupied()
                        valid_destination = True
                        #jail behavior

                    else:
                        destination_column = input('Please enter valid column: ')
                else:
                    destination_column = input('Please enter valid column: ')

            self.dice.remove(abs(int(destination_column) - int(origin_column)))
            self.board.columns_ascii = []
            self.board.create_board()


    
    


