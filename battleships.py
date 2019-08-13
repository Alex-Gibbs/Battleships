def make_board(grid_size): 
    board = []
    for i in range(grid_size):
        board.append([])
    for y in board:  
        for x in range(grid_size):
            y.append('~')
                
    return board
            

def place_ship(ship, board, x, y):
    print(f'Direction: {direction}')
    print(f'Ship Length: {ship}')
    print(f'Coordinate: {coord}')
    return board

def check_coordinate(coordinate, grid_size):
    pass


ship_girths = [2, 3, 4, 5]

check_coord = True

board = make_board(grid_size=10)
for ship in ship_girths:
    while check_coord:     
        coord =  input('Please enter a coordinate, in format x, y: ')  
        try:
            coord = coord.replace(' ', '').split(',')
            x = int(coord[0])
            y = int(coord[1])
        except Exception:
            print('Invalid Coordinate')
        else: 
            place_ship(ship, board, x, y)  
            check_coord = False
    check_coord = True 
        


for line in board:
    print(line)


    