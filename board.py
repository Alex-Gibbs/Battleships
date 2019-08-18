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

    def place_ship(self, ship, x, y, direction):
        print(f'Coordinate: {x, y}')
        print(f'Direction: {direction}')
        if direction == 'h':
            for i in range(ship.length):
                self.is_coord_on_board(x + i, y)
                if self.board[self.grid_size - (y - 1) - 1][x - 1 + i] == 'X':
                    raise ValueError

            for i in range(ship.length):
                ship.add_coordinate([x + i, y])
                self.board[self.grid_size - (y - 1) - 1][x - 1 + i] = 'X'
        else:
            for i in range(ship.length):
                self.is_coord_on_board(x, y + i)
                if self.board[self.grid_size - (y - 1) - 1 - i][x - 1] == 'X':
                    raise ValueError

            for i in range(ship.length):
                ship.add_coordinate([x, y + i])
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
                    direction = input(f'Please enter a direction for ship {ship.index} (h or v): ')
                    self.is_direction_valid(direction)
                    self.place_ship(ship, x, y, direction)
                except (IndexError, ValueError):
                    print('INVALID SHIP PLACEMENT!')
                else:
                    check_coord = False
            check_coord = True
            print(f'Ship {ship.index} placed!')

        self.print_board()
        print("All ships placed!")

    def update_guess_board(self, coordinate, is_hit):
        if is_hit:
            self.board[self.grid_size - (coordinate[1] - 1) - 1][coordinate[0] - 1] = 'X'
        else:
            self.board[self.grid_size - (coordinate[1] - 1) - 1][coordinate[0] - 1] = 'O'

    def attempt_attack(self, coordinate):
        for ship in self.list_of_ships:
            successful_attack = ship.attack_ship(coordinate)
            if successful_attack:
                if ship.is_sunk():
                    self.list_of_ships.remove(ship)
                return successful_attack
        print("You missed my battleships...")
        return False

    def make_guess(self):
        check_coordinate = True
        while check_coordinate:
            try:
                attack_coordinate = input("Please enter an attack coordinate, in format x, y: ")
                attack_coordinate = attack_coordinate.replace(' ', '').split(',')
                x = int(attack_coordinate[0])
                y = int(attack_coordinate[1])
                self.is_coord_on_board(x, y)
            except (IndexError, ValueError):
                print('INVALID COORDINATE!')
            else:
                check_coordinate = False

        is_hit = self.attempt_attack([int(x), int(y)])
        return [int(x), int(y)], is_hit

    def all_ships_sunk(self):
        if not self.list_of_ships:
            return True
        else:
            return False


    def print_board(self):
        for line in self.board:
            print(line)
