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
        self.blocks = self._pack_to_1d_arr(
            self.hours_blocks, self.mins_blocks, self.secs_blocks)

    def _pack_to_1d_arr(self, *args):
        arr = []
        for row in args:
            for blocks in row:
                for block in blocks:
                    arr.append(block)
        return arr

    def draw(self, surface):
        for block in self.blocks:
            block.draw(surface)

    def _update_hours(self, time):
        hours = time.split(':')[0]
        hours_bin_first = bin(int(hours) // 10).split('b')[1][::-1]
        for i in range(len(hours_bin_first)):
            self.hours_blocks[0][i].state = int(hours_bin_first[i])

        hours_bin_second = bin(int(hours) % 10).split('b')[1][::-1]
        for i in range(len(hours_bin_second)):
            self.hours_blocks[1][i].state = int(hours_bin_second[i])

    def _update_mins(self, time):
        mins = time.split(':')[1]
        mins_bin_first = bin(int(mins) // 10).split('b')[1][::-1]
        for i in range(len(mins_bin_first)):
            self.mins_blocks[0][i].state = int(mins_bin_first[i])

        mins_bin_second = bin(int(mins) % 10).split('b')[1][::-1]
        for i in range(len(mins_bin_second)):
            self.mins_blocks[1][i].state = int(mins_bin_second[i])

    def _update_secs(self, time):
        secs = time.split(':')[2]
        secs_bin_first = bin(int(secs) // 10).split('b')[1][::-1]
        for i in range(len(secs_bin_first)):
            self.secs_blocks[0][i].state = int(secs_bin_first[i])

        secs_bin_second = bin(int(secs) % 10).split('b')[1][::-1]
        for i in range(len(secs_bin_second)):
            self.secs_blocks[1][i].state = int(secs_bin_second[i])

    def update(self):
        for block in self.blocks:
            block.state = 0
        time = datetime.now().strftime('%H:%M:%S')
        self._update_hours(time)
        self._update_mins(time)
        self._update_secs(time)
