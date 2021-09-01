import pygame

from snake_game.snake import Snake
from snake_game.cube import Cube

from snake_game.functions import redraw_window, generate_snack, message_box


def main():
    size = 500   # field needs to be square
    rows = 20
    win = pygame.display.set_mode((size, size))
    snake = Snake((255, 0, 0), (10, 10))
    snack = Cube(generate_snack(rows, snake), color=(0, 255, 0))
    clock = pygame.time.Clock()

    while True:
        pygame.time.delay(50)
        clock.tick(10)
        snake.move()
        if snake.body[0].pos == snack.pos:
            snake.add_cube()
            snack = Cube(generate_snack(rows, snake), color=(0, 255, 0))
        redraw_window(snake, snack, rows, size, win)

        for x in range(len(snake.body)):
            if snake.body[x].pos in list(map(lambda z: z.pos, snake.body[x + 1:])):
                print('You lost!')
                print(f'Score: {len(snake.body)}')
                message_box("\'You Lost!\'", "\'Play again...\'")
                snake.reset((10, 10))
                break

        redraw_window(snake, snack, rows, size, win)


if __name__ == "__main__":
    main()
