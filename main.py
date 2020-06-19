import pygame as pg
import sys
import binary_clock.binary_clock as bin_clock
pg.init()
surface_size = (800, 600)
background = (0, 255, 0)
surface = pg.display.set_mode(surface_size)
binary_clock = bin_clock.Binary_Clock(pg.Vector2(100, 100))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    surface.fill(background)
    binary_clock.update()
    binary_clock.draw(surface)
    pg.display.flip()
