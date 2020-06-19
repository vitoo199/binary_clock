import pygame as pg


class Grid():
    def __init__(self, cell_size, ):
        self.cell_size = cell_size

    def place(self, init_pos, pos):
        return pg.Vector2(init_pos.x + pos.x * self.cell_size.x*2,
                          init_pos.y + pos.y * self.cell_size.y*2)
