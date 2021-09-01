import pygame
import random
import tkinter as tk
from tkinter import messagebox


def draw_grid(rows, size, surface):
    x, y = 0, 0
    cell_size = size//rows

    for _ in range(rows):
        x += cell_size
        y += cell_size
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, size))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (size, y))


def redraw_window(snake, snack, rows, size, surface):
    surface.fill((0, 0, 0))
    draw_grid(rows, size, surface)
    snake.draw(surface)
    snack.draw(surface)
    pygame.display.update()


def generate_snack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return x, y


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    root.destry()
