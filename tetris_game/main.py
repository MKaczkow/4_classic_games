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


def main():
    pass


def main_menu():
    pass


pygame.font.init()
main_menu()
