class unit():

    def __init__(self):
        self.unit_name = 'Droid'

    def unit_values(self):
        self.hitpoints = 100
        self.armor = 3
        self.attak = 6
        self.speed = 5
        self.min_range = 0
        self.max_range = 1

    def movment(self):
        self.north = 1
        self.south = -1
        self.west = -1
        self.east = 1
