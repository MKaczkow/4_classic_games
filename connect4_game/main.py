import pygame

from connect4_game.functions import (
    create_board,
    drop_piece,
    is_valid_location,
    get_next_open_row,
    print_board,
    winning_move
)
from connect4_game.config import ROW_COUNT, COLUMN_COUNT, PLAYER_0, PLAYER_1

board = create_board(ROW_COUNT, COLUMN_COUNT)
game_over = False
player_zero_turn = True

# main game loop
while not game_over:

    if player_zero_turn:
        column = int(input("Player 0: make your selection from columns 0 to 5\n"))
        player_zero_turn = not player_zero_turn

        if is_valid_location(board, column, ROW_COUNT):
            row = get_next_open_row(board, column)
            drop_piece(board, row, column, PLAYER_0)

            if winning_move(board, PLAYER_0):
                game_over = True
                print('PLAYER_0 wins!')

    else:
        column = int(input("Player 1: make your selection from columns 0 to 5\n"))
        player_zero_turn = not player_zero_turn

        if is_valid_location(board, column, ROW_COUNT):
            row = get_next_open_row(board, column)
            drop_piece(board, row, column, PLAYER_1)

            if winning_move(board, PLAYER_1):
                game_over = True
                print('PLAYER_1 wins!')

    print_board(board)



