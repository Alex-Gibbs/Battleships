from board import Board
from ship import Ship
from os import system, name
from time import sleep

def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')



""" Main method """
if __name__ == '__main__':
    # Game setup
    ship_1 = Ship(1, 2)
    ship_2 = Ship(2, 3)
    ship_3 = Ship(3, 3)
    ship_4 = Ship(4, 4)
    ship_5 = Ship(5, 5)
    GRID_SIZE = 10
    player_1_board = Board(GRID_SIZE, [ship_1, ship_2, ship_3, ship_4, ship_5])
    player_2_board = Board(GRID_SIZE, [ship_1, ship_2, ship_3, ship_4, ship_5])
    print("Player 1 get ready to position your battleships!")
    input("Press Enter to continue...")
    player_1_board.set_ships()
    sleep(2)
    clear_screen()
    print("Player 2 get ready to position your battleships!")
    input("Press Enter to continue...")
    player_2_board.set_ships()
    sleep(2)
    clear_screen()


