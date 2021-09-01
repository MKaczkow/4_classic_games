import pygame


class Cube(object):

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color
        self.rows = 20
        self.size = 500

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos(self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        cell_size = self.size//self.size

        pygame.draw.rect(surface,
                         self.color,
                         (self.pos[0]*cell_size + 1, self.pos[1]*cell_size + 1, cell_size -2, cell_size +2))

        if eyes:
            pass