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

            possible_destinations = self.generate_possible_destinations(int(origin_column))

            while valid_origin == False:
                if self.board.columns[int(origin_column) - 1].color_status == self.player.color:
                    if self.check_possible_destinations(possible_destinations):
                        print('we are here')
                        valid_origin = True
                    else:
                        print("you found me")
                        origin_column = input('Please enter valid origin column: ')
                        possible_destinations = self.generate_possible_destinations(int(origin_column))
                else:
                    origin_column = input('Please enter valid origin column: ')
                    possible_destinations = self.generate_possible_destinations(int(origin_column))

            destination_column = input('Which column would you like to move to? ')

            
            while valid_destination == False:
                
                if int(destination_column) - int(origin_column) > 0:
                    check_direction = 'up'
                else:
                    check_direction = 'down'

                if abs(int(destination_column) - int(origin_column)) in self.dice:

                    if (self.board.columns[int(destination_column) - 1].color_status == self.player.color or self.board.columns[int(destination_column) - 1].color_status == "None") and (self.player.direction == check_direction):
                        print('add')
                        
                        self.board.columns[int(destination_column) - 1].num_pieces += 1
                        self.board.columns[int(origin_column) - 1].num_pieces -= 1
                        if self.board.columns[int(origin_column) - 1].num_pieces == 0:
                            self.board.columns[int(origin_column) - 1].color_status = "None"
                        self.board.columns[int(destination_column) - 1].color_status = self.player.color
                        for i in range(24):
                            self.board.columns[i].set_occupied()
                        valid_destination = True

                    elif (self.board.columns[int(destination_column) - 1].color_status != self.player.color) and (self.board.columns[int(destination_column) - 1].occupied == False) and (self.player.direction == check_direction):
                        print("doesn't add")
                        self.board.columns[int(origin_column) - 1].num_pieces -= 1
                        self.board.columns[int(destination_column) - 1].color_status = self.player.color
                        if self.board.columns[int(origin_column) - 1].num_pieces == 0:
                            self.board.columns[int(origin_column) - 1].color_status = "None"
                        for i in range(24):
                            self.board.columns[i].set_occupied()
                        valid_destination = True
                        #jail behavior

                    else:
                        destination_column = input('Please enter valid destination column: ')
                else:
                    destination_column = input('Please enter valid destination column: ')

            self.dice.remove(abs(int(destination_column) - int(origin_column)))
            self.board.columns_ascii = []
            self.board.create_board()



    def generate_possible_destinations(self, origin_column):
        possible_destinations = []
        for i in self.dice:
            if self.player.direction == 'up':
                possible_destinations.append(origin_column + i)
            elif self.player.direction == 'down':
                possible_destinations.append(origin_column - i)
        return possible_destinations
    
    def check_possible_destinations(self, possible_destinations):
        # two possible set of things could be true:
        # 1. the destination col is our color OR none
        # OR
        # 2. the destination col is not our color AND not occupied
        truth_values = []
        for j in possible_destinations:
            if (self.board.columns[j - 1].color_status == (self.player.color or "None")) or (self.board.columns[j - 1].color_status != self.player.color and self.board.columns[j - 1].occupied == False):
                truth_values.append(True)
            else:
                truth_values.append(False)
        return any(truth_values)

    
