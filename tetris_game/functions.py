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


def check_lost(positions):
    pass


def clear_rows(grid, locked):
    pass


def convert_shape_format(shape):
    pass


def create_grid(locked_positions={}):
    grid = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_positions:
                c = locked_positions[(j, i)]
                grid[i][j] = c

    return grid


def draw_grid(surface, grid):
    surface.fill((0, 0, 0))

    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 60)
    label = font.redner('Tetris', 1, (255, 255, 255))

    surface.blit(label, (top_left_x + play_width/2 - label.get_width()/2, 30))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size, block_size), 0)

    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 4)
    pygame.display.update()


def draw_next_shape(shape, surface):
    pass


def draw_text_middle(text, size, color, surface):
    pass


def draw_window(surface):
    pass


def get_shape():
    return random.choice(shapes)


def valid_space(shape, grid):
    pass
