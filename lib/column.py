
class Column:

    def __init__(self, number, num_pieces = 0, color_status = "None"):
        self.number = number
        self.num_pieces = num_pieces
        self.color_status = color_status

        self.set_occupied()
        
    def set_occupied(self):
        if self.num_pieces > 1:
            self.occupied = True
        else:
            self.occupied = False