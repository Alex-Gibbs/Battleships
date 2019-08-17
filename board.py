class Board:

    def __init__(self, grid_size, list_of_ships):
        self.grid_size = grid_size
        self.list_of_ships = list_of_ships
        self.board = self.make_board(self.grid_size)

    def make_board(self, grid_size):
        board = []
        for i in range(grid_size):
            board.append([])
        for y in board:
            for x in range(grid_size):
                y.append('~')

        return board

    def place_ship(self, ship_length, x, y, direction):
        print(f'Coordinate: {x, y}')
        print(f'Direction: {direction}')
        if direction == 'h':
            for i in range(ship_length):
                self.is_coord_on_board(x + i, y)
                if self.board[self.grid_size - (y - 1) - 1][x - 1 + i] == 'X':
                    raise ValueError

            for i in range(ship_length):
                self.board[self.grid_size - (y - 1) - 1][x - 1 + i] = 'X'
        else:
            for i in range(ship_length):
                self.is_coord_on_board(x, y + i)
                if self.board[self.grid_size - (y - 1) - 1 - i][x - 1] == 'X':
                    raise ValueError

            for i in range(ship_length):
                self.board[self.grid_size - (y - 1) - 1 - i][x - 1] = 'X'

    def is_coord_on_board(self, x, y):
        if 1 <= x <= self.grid_size and 1 <= y <= self.grid_size:
            pass
        else:
            raise ValueError

    def is_direction_valid(self, direction):
        if direction.lower() in ['h', 'horizontal', 'v', 'vertical']:
            pass
        else:
            raise ValueError

    def set_ships(self):
        check_coord = True

        for ship in self.list_of_ships:
            while check_coord:
                self.print_board()
                print(f'Place ship {ship.index}')
                print(f'Ship {ship.index} length: {ship.length}')
                try:
                    coord = input(f'Please enter a coordinate for ship {ship.index}, in format x, y: ')
                    coord = coord.replace(' ', '').split(',')
                    x = int(coord[0])
                    y = int(coord[1])
                    self.is_coord_on_board(x, y)
                    direction = input(f'Please enter a direction for ship {ship.index} (h or v):')
                    self.is_direction_valid(direction)
                    self.place_ship(ship.length, x, y, direction)
                except (IndexError, ValueError):
                    print('INVALID SHIP PLACEMENT\n')
                else:
                    check_coord = False
            check_coord = True
            print(f'Ship {ship.index} placed!')

        self.print_board()
        print("All ships placed!")

    def print_board(self):
        for line in self.board:
            print(line)
