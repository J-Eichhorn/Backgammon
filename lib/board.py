from move import Move
from column import Column
from player import Player

class Board:

    def __init__(self):
        self.columns = []
        self.columns_ascii = []

        self.create_columns()
        self.create_board()
    
    def create_columns(self):
        for i in range(24):
            self.columns.append(Column(i + 1))

    def create_board(self):
        # board = '''
        # ========================================================================
        # |  {}     {}     {}     {}     {}     {}     {}     {}     {}    {}    {}    {} |
        # |                                                                      |
        # |                                                                      |
        # |                                                                      |
        # |                                                                      |
        # |                                                                      |
        # |                                                                      |
        # |                                                                      |
        # |                                                                      |
        # |                                                                      |
        # |                                                                      |
        # |                                                                      |
        # | {}    {}    {}    {}    {}    {}    {}    {}    {}    {}    {}    {} |
        # ========================================================================


        # '''.format(*[column.number for column in self.columns], sep = ",")
        # print(board)

        for x in range(12):
            self.columns_ascii.append([self.columns[x].number, '*', '*', '*', '*', '*', '','*', '*', '*', '*', '*', self.columns[23-x].number])

            
            for piece in self.columns[x].num_pieces:
                self.columns_ascii[piece]
            self.columns[23-x].num_pieces

        self.columns_ascii.reverse()
        for row in range(13):
            print('{:^6} {:^6} {:^6} {:^6} {:^6} {:^6} |    | {:^6} {:^6} {:^6} {:^6} {:^6} {:^6}'.format(*[column[row] for column in self.columns_ascii], sep = ","))
