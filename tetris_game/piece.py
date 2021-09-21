import pygame
import random

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


class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape.colors[shapes.index[shape]]
        self.rotation = 0
