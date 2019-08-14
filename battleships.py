def make_board(grid_size): 
    board = []
    for i in range(grid_size):
        board.append([])
    for y in board:  
        for x in range(grid_size):
            y.append('~')
                
    return board
            
def place_ship(ship, board, x, y):
    # print(f'Direction: {direction}')
    print(f'Ship Length: {ship}')
    print(f'Coordinate: {coord}')
    for i in range(ship):
        if board[len(board) - (y - 2) - i][x - 1] == 'X':
            raise ValueError

    for i in range(ship):
        board[len(board) - (y - 2) - i][x - 1] = 'X'
            
    return board

def check_ship_len(x, y, ship_length, grid_size):
    return not(y + ship_length - 1 > grid_size)

def is_coord_on_board(x, y, grid_size):
    if 1 <= x <= grid_size and 1 <= y <= grid_size:
        pass 
    else:
        raise ValueError

ship_lengths = [2, 3, 4, 5]
grid_size = 10 
check_coord = True

board = make_board(grid_size=grid_size)
for ship in ship_lengths:
    while check_coord:     
        coord =  input('Please enter a coordinate, in format x, y: ')  
        try:
            coord = coord.replace(' ', '').split(',')
            x = int(coord[0])
            y = int(coord[1])
            is_coord_on_board(x=x, y=y, grid_size=grid_size)    
            place_ship(ship, board, x, y)  
        except (IndexError, ValueError):
            print('Invalid Coordinate\n')
        else: 
            check_coord = False
    check_coord = True 
        
for line in board:
    print(line)


    