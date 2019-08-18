class Ship:

    def __init__(self, index, length):
        self.index = index
        self.length = length
        self.coordinates = []

    def add_coordinate(self, coordinate):
        self.coordinates.append(coordinate)

    def is_hit(self, coordinate):
        if coordinate in self.coordinates:
            return True
        else:
            return False

    def is_sunk(self):
        if not self.coordinates:
            print("You sunk my battleship!")
            return True
        else:
            return False

    def attack_ship(self, coordinate):
        if self.is_hit(coordinate):
            print("You hit my battleship!")
            self.coordinates.remove(coordinate)
            return True
        else:
            return False
