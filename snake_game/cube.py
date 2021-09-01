import pygame


class Cube(object):

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        self.pos = start
        self.dirnx = dirnx
        self.dirny = dirny
        self.color = color
        self.rows = 20
        self.size = 500

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        cell_size = self.size//self.rows

        pygame.draw.rect(surface,
                         self.color,
                         (self.pos[0]*cell_size + 1, self.pos[1]*cell_size + 1, cell_size - 2, cell_size - 2))

        if eyes:
            center = cell_size//2
            radius = 3
            first_eye = (self.pos[0]*cell_size + center - radius, self.pos[1]*cell_size + 8)
            second_eye = (self.pos[0]*cell_size + cell_size - radius*2, self.pos[0]*cell_size + 8)
            pygame.draw.circle(surface, (0, 0, 0), first_eye, radius)
            pygame.draw.circle(surface, (0, 0, 0), second_eye, radius)

