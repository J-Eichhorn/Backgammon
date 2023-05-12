
class Player:

    player_list = []

    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

        Player.player_list.append(self)
        self.choose_color()

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            raise Exception("Please enter a valid name.")
        
    name = property(get_name, set_name)

    def choose_color(self):
        if len(Player.player_list) == 1:
            self.color = 'red'
            self.direction = 'up'
        else:
            self.color = 'white'
            self.direction = 'down'
