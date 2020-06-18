import pygame as pg


class Block():
    def __init__(self, pos, size, state=0):
        self.pos = pos
        self.state = state
        self.size = size
        self.rect = pg.Rect(pos, self.size)
        self.color_active = (0, 0, 255)
        self.color_not_active = (0, 0, 0)

    def draw(self, surface):
        state_color = self.color_active if self.state else self.color_not_active
        pg.draw.rect(surface, state_color, self.rect)
