class Board:

    def __init__(self, grid_size, list_of_ship_lengths):
        self.grid_size = grid_size
        self.list_of_ship_lengths = list_of_ship_lengths
        self.board = self.make_board(self.grid_size)

    def make_board(self, grid_size):
        board = []
        for i in range(grid_size):
            board.append([])
        for y in board:
            for x in range(grid_size):
                y.append('~')

        return board

    def place_ship(self, ship_length, board, x, y, direction):
        print(f'Ship Length: {ship_length}')
        print(f'Coordinate: {x, y}')
        print(f'Direction: {direction}')
        if direction == 'h':
            for i in range(ship_length):
                if self.board[self.grid_size - (y - 1) - 1][x - 1 + i] == 'X':
                    raise ValueError

            for i in range(ship_length):
                self.board[self.grid_size - (y - 1) - 1][x - 1 + i] = 'X'
        else:
            for i in range(ship_length):
                if self.board[self.grid_size - (y - 1) - 1 - i][x - 1] == 'X':
                    raise ValueError

            for i in range(ship_length):
                self.board[self.grid_size - (y - 1) - 1 - i][x - 1] = 'X'

    def check_ship_len(self, x, y, list_of_ship_lengths):
        return not (y + list_of_ship_lengths - 1 > self.grid_size)

    def is_coord_on_board(self, x, y):
        if 1 <= x <= self.grid_size and 1 <= y <= self.grid_size:
            pass
        else:
            raise ValueError

    def set_ships(self):
        check_coord = True

        for ship in self.list_of_ship_lengths:
            while check_coord:
                coord = input('Please enter a coordinate, in format x, y: ')
                try:
                    coord = coord.replace(' ', '').split(',')
                    x = int(coord[0])
                    y = int(coord[1])
                    self.is_coord_on_board(x=x, y=y)
                    direction = input('Please enter a direction (h or v):')
                    self.place_ship(ship, self.board, x, y, direction)
                except (IndexError, ValueError):
                    print('Invalid Coordinate\n')
                else:
                    check_coord = False
            check_coord = True

    def print_board(self):
        for line in self.board:
            print(line)


""" Main method """
if __name__ == '__main__':
    battleship_board = Board(10, [2, 3, 3, 4, 5])
    battleship_board.set_ships()
    print(battleship_board)
