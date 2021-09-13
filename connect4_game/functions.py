import numpy as np
from connect4_game.config import ROW_COUNT, COLUMN_COUNT


def create_board(row_count, column_count):
    board = np.zeros((row_count, column_count))
    return board


def drop_piece(board, row, column, piece):
    board[row][column] = piece


def is_valid_location(board, column, row_count):
    return not board[row_count - 1][column]


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if not board[r][col]:
            return r


def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):

    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece \
                    and board[r][c + 1] == piece \
                    and board[r][c + 2] == piece \
                    and board[r][c + 3] == piece:
                return True

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece \
                    and board[r + 1][c] == piece \
                    and board[r + 2][c] == piece \
                    and board[r + 3][c] == piece:
                return True

    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece \
                    and board[r + 1][c + 1] == piece\
                    and board[r + 2][c + 2] == piece \
                    and board[r + 3][c + 3] == piece:
                return True

    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece \
                    and board[r - 1][c + 1] == piece\
                    and board[r - 2][c + 2] == piece \
                    and board[r - 3][c + 3] == piece:
                return True

