import pygame
import random

from tetris_game.piece import Piece
from tetris_game.functions import  (
    check_lost,
    clear_rows,
    convert_shape_format,
    create_grid,
    draw_grid,
    draw_next_shape,
    draw_text_middle,
    draw_window,
    get_shape,
    valid_space
)
from tetris_game.config import (
    s_height,
    s_width,
    play_height,
    play_width,
    block_size,
    top_left_x,
    top_left_y,
    shapes,
    shape_colors
)

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""


def main(surface):

    locked_positions = {}
    grid = create_grid(locked_positions)
    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.typ == pygame.LEFT:
                    current_piece.x -= 1
                    if valid_space(current_piece.x, grid):
                        current_piece.x += 1

                if event.typ == pygame.K_RIGHT:
                    current_piece.x += 1
                    if valid_space(current_piece, grid):
                        current_piece.x -= 1

                if event.typ == pygame.K_UP:
                    current_piece.y += 1
                    if valid_space(current_piece, grid):
                        current_piece.y -= 1

                if event.typ == pygame.K_DOWN:
                    current_piece.rotation += 1
                    if valid_space(current_piece, grid):
                        current_piece.rotation -= 1

        draw_window(surface, grid)


def main_menu():
    pass


pygame.font.init()
main_menu()
