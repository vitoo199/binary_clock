import pygame as pg
import sys

pg.init()
screen_size = (800, 600)
background = (255, 255, 255)
screen = pg.display.set_mode(screen_size)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        screen.fill(background)
        pg.display.flip()
