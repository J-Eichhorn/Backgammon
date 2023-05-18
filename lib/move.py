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
        self.roll_dice()

    def roll_dice(self):
        self.dice.append(random.randint(1,6))
        self.dice.append(random.randint(1,6))

    def user_move(self):
        # add doubles behavior
        
        turn = 0
        turn_over = False
        while turn < 2:

            if len(self.dice) == 2:
                time.sleep(1)
                print(f"Your turn, {self.player.name}!")
                time.sleep(1)
                print(f'You rolled: {*self.dice,}')
            else:
                time.sleep(1)
                print(f'Still your turn, {self.player.name}!')
                time.sleep(1)
                print(f'Your remaining roll: ({self.dice[0]})')

            valid_origin = False
            valid_destination = False

            if self.player.color not in Move.jail:
                time.sleep(1)
                origin_column = input('Which column would you like to move from? ')
            else:
                if self.player.color == 'red':
                    origin_column = 0
                elif self.player.color == 'white':
                    origin_column = 25

            possible_destinations = self.generate_possible_destinations(int(origin_column))

            while valid_origin == False:
                if self.player.color in Move.jail:
                    print(possible_destinations)
                    if self.check_possible_destinations(possible_destinations):
                        Move.jail.remove(self.player.color)
                        valid_origin = True
                    else: 
                        time.sleep(1)
                        print(f'Sorry {self.player.name}, no available moves!')
                        time.sleep(2)
                        turn_over = True
                        break
                elif self.board.columns[int(origin_column) - 1].color_status == self.player.color:
                    if self.check_possible_destinations(possible_destinations):
                        valid_origin = True
                    else:
                        origin_column = input('Please enter valid origin column: ')
                        possible_destinations = self.generate_possible_destinations(int(origin_column))
                else:
                    origin_column = input('Please enter valid origin column: ')
                    possible_destinations = self.generate_possible_destinations(int(origin_column))

            if turn_over == True:
                turn = 2
                self.clear()
                self.board.columns_ascii = []
                self.board.create_board()
                break
            else:
                destination_column = input('Which column would you like to move to? ')

            
            while valid_destination == False:

                if destination_column == 'off':
                    if self.allowed_off():
                        possible_destinations = self.generate_possible_destinations(int(origin_column))
                        if len(self.dice) == 2:
                            if (possible_destinations[0] > 24 or possible_destinations[0] < 1) or (possible_destinations[1] > 24 or possible_destinations[1] < 1):
                                dice_input = int(input('Which die roll do you want to use? '))
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
                        destination_column = input('Please enter valid destination column: ')

                elif abs(int(destination_column) - int(origin_column)) in self.dice:

                    if int(destination_column) - int(origin_column) > 0:
                        check_direction = 'up'
                    else:
                        check_direction = 'down'

                    if (self.board.columns[int(destination_column) - 1].color_status == self.player.color or self.board.columns[int(destination_column) - 1].color_status == "None") and (self.player.direction == check_direction):
                        self.board.columns[int(destination_column) - 1].num_pieces += 1
                        self.board.columns[int(destination_column) - 1].color_status = self.player.color
                        self.maneuver_pieces(origin_column)

                        valid_destination = True

                    elif (self.board.columns[int(destination_column) - 1].color_status != self.player.color) and (self.board.columns[int(destination_column) - 1].occupied == False) and (self.player.direction == check_direction):
                        self.board.columns[int(destination_column) - 1].color_status = self.player.color
                        self.maneuver_pieces(origin_column)

                        Move.jail.append([player.color for player in Player.player_list if player.color != self.player.color][0])
                        print(Move.jail)

                        valid_destination = True

                    else:
                        destination_column = input('Please enter valid destination column: ')
                else:
                    destination_column = input('Please enter valid destination column: ')

            if destination_column == 'off':
                self.dice.remove(dice_input)
            else:
                self.dice.remove(abs(int(destination_column) - int(origin_column)))
            self.clear()
            self.board.columns_ascii = []
            self.board.create_board()
            turn += 1



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
    
    def maneuver_pieces(self, origin_column):
        self.board.columns[int(origin_column) - 1].num_pieces -= 1
        if self.board.columns[int(origin_column) - 1].num_pieces == 0:
            self.board.columns[int(origin_column) - 1].color_status = "None"
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

