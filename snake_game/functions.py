import pygame


def draw_grid(rows, size, surface):
    x, y = 0, 0
    cell_size = size//rows

    for _ in range(rows):
        x += cell_size
        y += cell_size
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, size))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (size, y))


def redraw_window(snake, rows, size, surface):
    surface.fill((0, 0, 0))
    draw_grid(rows, size, surface)
    snake.draw(surface)
    pygame.display.update()
