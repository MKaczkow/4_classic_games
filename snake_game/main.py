import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

from snake_game.snake import Snake
from snake_game.cube import Cube

from snake_game.functions import *


def main():
    size = 500   # field needs to be square
    rows = 20
    win = pygame.display.set_mode((size, size))
    s = Snake((255, 0, 0), (10, 10))

    clock = pygame.time.Clock()

    while True:
        pygame.time.delay(50)
        clock.tick(10)
        redraw_window(s, rows, size, win)


if __name__ == "__main__":
    main()
