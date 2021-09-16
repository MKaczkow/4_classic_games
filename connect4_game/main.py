import pygame
import sys
import math

from connect4_game.functions import (
    create_board,
    drop_piece,
    is_valid_location,
    get_next_open_row,
    print_board,
    winning_move,
    draw_board
)
from connect4_game.config import (
    ROW_COUNT,
    COLUMN_COUNT,
    RADIUS,
    PLAYER_0,
    PLAYER_1,
    SQUARESIZE,
    BLACK,
    YELLOW,
    RED
)


board = create_board(ROW_COUNT, COLUMN_COUNT)
game_over = False
player_zero_turn = True

pygame.init()

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE

size = (width, height)

screen = pygame.display.set_mode(size)
draw_board(board, screen)
pygame.display.update()

# main game loop
while not game_over:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            if player_zero_turn:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            posx = event.pos[0]
            column = int(math.floor(posx / SQUARESIZE))

            if player_zero_turn:
                player_zero_turn = not player_zero_turn

                if is_valid_location(board, column, ROW_COUNT):
                    row = get_next_open_row(board, column)
                    drop_piece(board, row, column, PLAYER_0)

                    if winning_move(board, PLAYER_0):
                        game_over = True
                        print('PLAYER_0 wins!')

            else:
                player_zero_turn = not player_zero_turn

                if is_valid_location(board, column, ROW_COUNT):
                    row = get_next_open_row(board, column)
                    drop_piece(board, row, column, PLAYER_1)

                    if winning_move(board, PLAYER_1):
                        game_over = True
                        print('PLAYER_1 wins!')

            # print_board(board)
            draw_board(board, screen)

            if game_over:
                pygame.time.wait(5000)
