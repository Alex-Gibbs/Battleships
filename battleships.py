def make_board(grid_size): 
    board = []
    for i in range(grid_size):
        board.append([])
    for y in board:  
        for x in range(grid_size):
            y.append('~')
                
    return board
            

def place_ship(ship, board, coord):
    print(f'Ship Length: {ship}')
    print(f'Coordinate: {coord}')
    return board

ship_girths = [2, 3, 4, 5]



board = make_board(grid_size=10)
for ship in ship_girths:
    coord =  input('Please enter a coordinate: ')
    place_ship(ship, board, coord)
    

for line in board:
    print(line)


