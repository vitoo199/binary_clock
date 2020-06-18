import pygame as pg
from binary_clock.block import Block
from datetime import datetime


class Binary_Clock():
    def __init__(self, pos):
        self.current_time = 0
        self.pos = pos
        self.margin = 100
        self.block_size = pg.Vector2(50, 50)
        self.hours_blocks = (
            (Block(pg.Vector2(self.pos.x, self.pos.y +
                              self.margin * 3), self.block_size, 0),
             Block(pg.Vector2(self.pos.x, self.pos.y +
                              self.margin * 2), self.block_size, 0)
             ),
            (
                Block(pg.Vector2(self.pos.x + self.margin,
                                 self.pos.y + self.margin * 3), self.block_size, 0),
                Block(pg.Vector2(self.pos.x + self.margin,
                                 self.pos.y + self.margin * 2), self.block_size, 0),
                Block(pg.Vector2(self.pos.x + self.margin,
                                 self.pos.y + self.margin * 1), self.block_size, 0),
                Block(pg.Vector2(self.pos.x + self.margin,
                                 self.pos.y), self.block_size, 0),
            )

        )
        self.mins_blocks = (
            (Block(pg.Vector2(self.pos.x + self.margin * 2, self.pos.y +
                              self.margin * 3), self.block_size, 0),
             Block(pg.Vector2(self.pos.x + self.margin * 2, self.pos.y +
                              self.margin * 2), self.block_size, 0),
             Block(pg.Vector2(self.pos.x + self.margin * 2, self.pos.y +
                              self.margin * 1), self.block_size, 0)
             ),
            (
                Block(pg.Vector2(self.pos.x + self.margin * 3,
                                 self.pos.y + self.margin * 3), self.block_size, 0),
                Block(pg.Vector2(self.pos.x + self.margin * 3,
                                 self.pos.y + self.margin * 2), self.block_size, 0),
                Block(pg.Vector2(self.pos.x + self.margin * 3,
                                 self.pos.y + self.margin * 1), self.block_size, 0),
                Block(pg.Vector2(self.pos.x + self.margin * 3,
                                 self.pos.y), self.block_size, 0),
            )

        )
        self.secs_blocks = (
            (Block(pg.Vector2(self.pos.x + self.margin * 4, self.pos.y +
                              self.margin * 3), self.block_size, 0),
             Block(pg.Vector2(self.pos.x + self.margin * 4, self.pos.y +
                              self.margin * 2), self.block_size, 0),
             Block(pg.Vector2(self.pos.x + self.margin * 4, self.pos.y +
                              self.margin * 1), self.block_size, 0)
             ),
            (
                Block(pg.Vector2(self.pos.x + self.margin * 5,
                                 self.pos.y + self.margin * 3), self.block_size, 0),
                Block(pg.Vector2(self.pos.x + self.margin * 5,
                                 self.pos.y + self.margin * 2), self.block_size, 0),
                Block(pg.Vector2(self.pos.x + self.margin * 5,
                                 self.pos.y + self.margin * 1), self.block_size, 0),
                Block(pg.Vector2(self.pos.x + self.margin * 5,
                                 self.pos.y), self.block_size, 0),
            )

        )

    def draw(self, surface):
        for row in self.hours_blocks:
            for hour_block in row:
                hour_block.draw(surface)
        for row in self.mins_blocks:
            for min_block in row:
                min_block.draw(surface)
        for row in self.secs_blocks:
            for sec_block in row:
                sec_block.draw(surface)

    def update(self):
        for row in self.secs_blocks:
            for sec_block in row:
                sec_block.state = 0
        now = datetime.now()

        hours = now.strftime("%H")
        hours_bin_first = bin(int(hours) // 10).split('b')[1][::-1]
        for i in range(len(hours_bin_first)):
            self.hours_blocks[0][i].state = int(hours_bin_first[i])

        hours_bin_second = bin(int(hours) % 10).split('b')[1][::-1]
        for i in range(len(hours_bin_second)):
            self.hours_blocks[1][i].state = int(hours_bin_second[i])

        mins = now.strftime("%M")
        mins_bin_first = bin(int(mins) // 10).split('b')[1][::-1]
        for i in range(len(mins_bin_first)):
            self.mins_blocks[0][i].state = int(mins_bin_first[i])

        mins_bin_second = bin(int(mins) % 10).split('b')[1][::-1]
        for i in range(len(mins_bin_second)):
            self.mins_blocks[1][i].state = int(mins_bin_second[i])

        secs = now.strftime("%S")
        secs_bin_first = bin(int(secs) // 10).split('b')[1][::-1]
        for i in range(len(secs_bin_first)):
            self.secs_blocks[0][i].state = int(secs_bin_first[i])

        secs_bin_second = bin(int(secs) % 10).split('b')[1][::-1]
        print(secs_bin_second)
        for i in range(len(secs_bin_second)):
            self.secs_blocks[1][i].state = int(secs_bin_second[i])
