from player import Player
import random
import os
import time

class Move:

    jail = []

    def __init__(self, board, player):
        self.board = board
        self.player = player

        self.dice = []
        self.turns = 2
        self.roll_dice()


    def roll_dice(self):
        self.dice[0:0] = [random.randint(1,6), random.randint(1,6)]
        if self.dice[0] == self.dice[1]:
            self.dice[2:2] = [self.dice[0]] * 2
            self.turns = 4

    def user_move(self):
        
        turn_count = 0
        turn_over = False
        while turn_count < self.turns: # this is the main loop that tells it how many turns to do

            if self.turns == 4: # script for doubles
                if len(self.dice) == 4:
                    time.sleep(1)
                    print(f"Your turn, {self.player.name} ({self.player.color.title()})!")
                    time.sleep(1)
                    print(f'You rolled: {*self.dice[0:2],}')
                    time.sleep(1)
                    print(f'You rolled doubles, {self.player.name}! You have {len(self.dice)} turns left!')
                elif len(self.dice) == 3 or len(self.dice) == 2:
                    time.sleep(1)
                    print(f'Still your turn, {self.player.name} ({self.player.color.title()})!')
                    time.sleep(1)
                    print(f'You rolled: {*self.dice[0:2],}')
                    time.sleep(1)
                    print(f'You rolled doubles, {self.player.name}! You have {len(self.dice)} turns left!')
                elif len(self.dice) == 1:
                    time.sleep(1)
                    print(f'One more turn, {self.player.name} ({self.player.color.title()})!')
                    time.sleep(1)
                    print(f'Your remaining roll: ({self.dice[0]})')
            elif self.turns == 2: # script for a regular turn
                if len(self.dice) == 2:
                    time.sleep(1)
                    print(f"Your turn, {self.player.name} ({self.player.color.title()})!")
                    time.sleep(1)
                    print(f'You rolled: {*self.dice,}')
                else:
                    time.sleep(1)
                    print(f'Still your turn, {self.player.name} ({self.player.color.title()})!')
                    time.sleep(1)
                    print(f'Your remaining roll: ({self.dice[0]})')

            valid_origin = False
            valid_destination = False

            valid_input1 = [str(x) for x in [*range(1,25)]]

            valid_input2 = [str(x) for x in [*range(1,25)]]
            valid_input2.append('off')

            # am i allowed to choose an origin?
            if self.player.color not in Move.jail: # player is not in jail
                if self.check_available_moves() == False: # but no available moves
                    time.sleep(1)
                    print(f'Sorry {self.player.name}, no available moves!')
                    time.sleep(2)
                    turn_count = self.turns
                    self.recreate_board()
                    break
                else:
                    time.sleep(1)
                    origin_column = self.get_column_number('origin', valid_input1, True)                  
            else: # player is in jail
                if self.player.color == 'red':
                    origin_column = 0
                elif self.player.color == 'white':
                    origin_column = 25
            possible_destinations = self.generate_possible_destinations(origin_column)

            # once i can choose an origin, is it valid?
            while valid_origin == False:
                if self.player.color in Move.jail: # player in jail
                    if self.check_possible_destinations(possible_destinations):
                        Move.jail.remove(self.player.color)
                        valid_origin = True
                    else: 
                        time.sleep(1)
                        print(f'Sorry {self.player.name}, no available moves!')
                        time.sleep(2)
                        turn_over = True
                        break
                elif self.board.columns[origin_column - 1].color_status == self.player.color: # player not in jail, valid origin
                    if self.check_possible_destinations(possible_destinations):
                        valid_origin = True
                    else:
                        origin_column = self.get_column_number('origin', valid_input1) 
                        possible_destinations = self.generate_possible_destinations(origin_column)
                else: # player not in jail, invalid origin
                    origin_column = self.get_column_number('origin', valid_input1) 
                    possible_destinations = self.generate_possible_destinations(origin_column)

            if turn_over == True:
                turn_count = self.turns
                self.recreate_board()
                break
            else:
                destination_column = self.get_column_number('destination', valid_input2, True) 

            # once i have a valid origin, is the destination that i choose valid?
            while valid_destination == False:

                if destination_column == 'off': # if you try to take piece 'off'
                    if self.allowed_off():
                        possible_destinations = self.generate_possible_destinations(origin_column)
                        if len(self.dice) >= 2:
                            if (possible_destinations[0] > 24 or possible_destinations[0] < 1) or (possible_destinations[1] > 24 or possible_destinations[1] < 1):
                                dice_input = input('Which die roll do you want to use? ')
                                while type(dice_input) != int:
                                    try:
                                        int(dice_input)
                                        dice_input = int(dice_input)
                                        if dice_input in self.dice:
                                            break
                                        else:
                                            dice_input = input('Please enter a valid die: ')
                                    except:
                                        dice_input = input('Please enter a valid die: ')


                                self.player.score += 1
                                self.maneuver_pieces(origin_column)
                                valid_destination = True
                                
                        elif len(self.dice) == 1:
                            if possible_destinations[0] > 24 or possible_destinations[0] < 1:
                                dice_input = self.dice[0]
                                self.player.score += 1
                                self.maneuver_pieces(origin_column)
                                valid_destination = True
                    else:
                        destination_column = self.get_column_number('destination', valid_input2) 

                elif abs(destination_column - origin_column) in self.dice: # if you enter a number
                    if destination_column - origin_column > 0:
                        check_direction = 'up'
                    else:
                        check_direction = 'down'

                    if (self.board.columns[destination_column - 1].color_status == self.player.color or self.board.columns[destination_column - 1].color_status == "None") and (self.player.direction == check_direction):
                        self.board.columns[destination_column - 1].num_pieces += 1
                        self.board.columns[destination_column - 1].color_status = self.player.color
                        self.maneuver_pieces(origin_column)

                        valid_destination = True

                    elif (self.board.columns[destination_column - 1].color_status != self.player.color) and (self.board.columns[destination_column - 1].occupied == False) and (self.player.direction == check_direction):
                        self.board.columns[destination_column - 1].color_status = self.player.color
                        self.maneuver_pieces(origin_column)

                        Move.jail.append([player.color for player in Player.player_list if player.color != self.player.color][0])
                        print(Move.jail)

                        valid_destination = True

                    else:
                        destination_column = self.get_column_number('destination', valid_input2) 
                else:
                    destination_column = self.get_column_number('destination', valid_input2) 

            if destination_column == 'off':
                self.dice.remove(dice_input)
            else:
                self.dice.remove(abs(destination_column - origin_column))
            self.recreate_board()
            if self.player.score == 15:
                turn_count = self.turns
            else:
                turn_count += 1



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
            if j > 24 or j < 1:
                if self.allowed_off():
                    truth_values.append(True)
            elif (self.board.columns[j - 1].color_status == (self.player.color or "None")) or (self.board.columns[j - 1].color_status != self.player.color and self.board.columns[j - 1].occupied == False):
                truth_values.append(True)
            else:
                truth_values.append(False)
        return any(truth_values)
    
    def check_available_moves(self):
        truth_values = []
        for column in self.board.columns:
            if column.color_status == self.player.color:
                possible_destinations = self.generate_possible_destinations(column.number)
                if self.check_possible_destinations(possible_destinations) == True:
                    truth_values.append(True)
                else:
                    truth_values.append(False)
        return any(truth_values)
    
    def maneuver_pieces(self, origin_column):
        self.board.columns[origin_column - 1].num_pieces -= 1
        if self.board.columns[origin_column - 1].num_pieces == 0:
            self.board.columns[origin_column - 1].color_status = "None"
        for i in range(24):
            self.board.columns[i].set_occupied()

    def clear(self):
        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')

    def allowed_off(self):
        if self.player.color == 'red':
            total = 0
            for i in range(18):
                if self.board.columns[i].color_status == 'red':
                    total += self.board.columns[i].num_pieces
            if total == 0:
                return True
        elif self.player.color == 'white':
            total = 0
            for i in range(18):
                if self.board.columns[23 - i].color_status == 'white':
                    total += self.board.columns[23 - i].num_pieces
            if total == 0:
                return True

    def recreate_board(self):
        self.clear()
        self.board.columns_ascii = []
        self.board.create_board()

    def get_column_number(self, type_column, valid_input, first = False):
        if first:
            if type_column == 'origin':
                column_number = input('Which column would you like to move from? ')
            elif type_column == 'destination':
                column_number = input('Which column would you like to move to? ')
        else: 
            column_number = input(f'Please enter valid {type_column} column: ')

        while column_number not in valid_input:
            column_number = input(f'Please enter valid {type_column} column: ') 

        try:
            int(column_number)
            return int(column_number)
        except:
            return column_number