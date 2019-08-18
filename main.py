from board import Board
from ship import Ship
from os import system, name
from time import sleep


def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def ordinary_battleships(player_1_board, player_2_board, player_1_guess_board, player_2_guess_board):
    has_player_1_won = False
    has_player_2_won = False
    while not has_player_1_won and not has_player_2_won:
        print("Player 1's turn...")
        player_1_guess_board.print_board()
        attack_coordinate, is_hit = player_2_board.make_guess()
        player_1_guess_board.update_guess_board(attack_coordinate, is_hit)
        has_player_1_won = player_2_board.all_ships_sunk()
        if has_player_1_won:
            print("Player 1 has won!")
            return

        print("Player 2's turn...")
        player_2_guess_board.print_board()
        attack_coordinate, is_hit = player_1_board.make_guess()
        player_2_guess_board.update_guess_board(attack_coordinate, is_hit)
        has_player_2_won = player_1_board.all_ships_sunk()
        if has_player_2_won:
            print("Player 2 has won!")
            return

if __name__ == '__main__':
    # Game setup
    player_1_ship_1 = Ship(1, 2)
    player_1_ship_2 = Ship(2, 3)
    player_1_ship_3 = Ship(3, 3)
    player_1_ship_4 = Ship(4, 4)
    player_1_ship_5 = Ship(5, 5)
    player_2_ship_1 = Ship(1, 2)
    player_2_ship_2 = Ship(2, 3)
    player_2_ship_3 = Ship(3, 3)
    player_2_ship_4 = Ship(4, 4)
    player_2_ship_5 = Ship(5, 5)
    GRID_SIZE = 10
    player_1_board = Board(GRID_SIZE,
                           [player_1_ship_1, player_1_ship_2, player_1_ship_3, player_1_ship_4, player_1_ship_5])
    player_2_board = Board(GRID_SIZE,
                           [player_2_ship_1, player_2_ship_2, player_2_ship_3, player_2_ship_4, player_2_ship_5])
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

    player_1_guess_board = Board(GRID_SIZE, [])
    player_2_guess_board = Board(GRID_SIZE, [])

    ordinary_battleships(player_1_board, player_2_board, player_1_guess_board, player_2_guess_board)
