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
    fall_speed = 0.27

    while run:

        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time/1000 > fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not(valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

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

        shape_pos = convert_shape_format(current_piece)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False

        draw_window(surface, grid)

        if check_lost(locked_positions):
            run = False

    pygame.display.quit()


def main_menu():

    main(surface)

if __name__ == "__main__":
    pygame.font.init()
    main_menu()
