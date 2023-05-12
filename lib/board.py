from move import Move
from column import Column
from player import Player

class Board:

    def __init__(self):
        self.columns = []
        self.columns_ascii = []

        self.create_columns()
        self.starting_position()
        self.create_board()
    
    def create_columns(self):
        for i in range(24):
            self.columns.append(Column(i + 1))

    def starting_position(self):
        self.columns[0].num_pieces = 2
        self.columns[0].color_status = 'red'
        self.columns[23].num_pieces = 2
        self.columns[23].color_status = 'white'
        self.columns[5].num_pieces = 5
        self.columns[5].color_status = 'white'
        self.columns[18].num_pieces = 5
        self.columns[18].color_status = 'red'
        self.columns[7].num_pieces = 3
        self.columns[7].color_status = 'white'
        self.columns[16].num_pieces = 3
        self.columns[16].color_status = 'red'
        self.columns[11].num_pieces = 5
        self.columns[11].color_status = 'red'
        self.columns[12].num_pieces = 5
        self.columns[12].color_status = 'white'
        self.columns[22].num_pieces = 10
        self.columns[22].color_status = 'red'

        for i in range(24):
            self.columns[i].set_occupied()
        

    def create_board(self):

        for x in range(12):

            self.columns_ascii.append([self.columns[x].number, '', self.columns[23-x].number])
                
            top_column = ['*', '*', '*', '*', '*']
            if self.columns[x].num_pieces <= 5:
                for i in range(self.columns[x].num_pieces):
                    if self.columns[x].color_status == 'red':  
                        top_column[i] = 'O'
                    elif self.columns[x].color_status == 'white':
                        top_column[i] = 'X'
            else:
                for i in range(4):
                    if self.columns[x].color_status == 'red':  
                        top_column[i] = 'O'
                    elif self.columns[x].color_status == 'white':
                        top_column[i] = 'X'
                top_column[4] = self.columns[x].num_pieces - 4
            self.columns_ascii[x][1:1] = top_column


            bottom_column = ['*', '*', '*', '*', '*']
            if self.columns[23 - x].num_pieces <= 5:
                for i in range(self.columns[23 - x].num_pieces):
                    if self.columns[23-x].color_status == 'red':  
                        bottom_column[4-i] = 'O'
                    elif self.columns[23-x].color_status == 'white':
                        bottom_column[4-i] = 'X'
            else:
                for i in range(4):
                    if self.columns[23-x].color_status == 'red':  
                        bottom_column[4-i] = 'O'
                    elif self.columns[23-x].color_status == 'white':
                        bottom_column[4-i] = 'X'
                bottom_column[0] = self.columns[23 - x].num_pieces - 4
            self.columns_ascii[x][-1:-1] = bottom_column  

        self.columns_ascii.reverse()
        dash = '=' * 90
        triangles = '/\\' * 45
        
        print(dash)
        print(triangles)
        print(dash)
        for row in range(13):
            print('{:^6} {:^6} {:^6} {:^6} {:^6} {:^6} |    | {:^6} {:^6} {:^6} {:^6} {:^6} {:^6}'.format(*[column[row] for column in self.columns_ascii], sep = ","))
        print(dash)
        print(triangles)
        print(dash)
        print('{:<}: {}/15  {:>68}: {}/15'.format(Player.player_list[0].name, Player.player_list[0].score, Player.player_list[1].name, Player.player_list[1].score))
        print(dash)

        