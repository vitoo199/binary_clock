import pygame as pg
from binary_clock.block import Block
from datetime import datetime
from binary_clock.grid import Grid


class Binary_Clock():
    def __init__(self, pos):
        self.pos = pos
        self.block_size = pg.Vector2(50, 50)
        self.grid = Grid(self.block_size)
        self.hours_blocks = (
            (Block(self.grid.place(self.pos, pg.Vector2(0, 4)), self.block_size, 0),
             Block(self.grid.place(self.pos, pg.Vector2(0, 3)), self.block_size, 0)
             ),
            (
                Block(self.grid.place(self.pos, pg.Vector2(1, 4)),
                      self.block_size, 0),
                Block(self.grid.place(self.pos, pg.Vector2(1, 3)),
                      self.block_size, 0),
                Block(self.grid.place(self.pos, pg.Vector2(1, 2)),
                      self.block_size, 0),
                Block(self.grid.place(self.pos, pg.Vector2(1, 1)),
                      self.block_size, 0),
            )

        )
        self.mins_blocks = (
            (Block(self.grid.place(self.pos, pg.Vector2(2, 4)), self.block_size, 0),
             Block(self.grid.place(self.pos, pg.Vector2(2, 3)), self.block_size, 0),
             Block(self.grid.place(self.pos, pg.Vector2(2, 2)), self.block_size, 0)
             ),
            (
                Block(self.grid.place(self.pos, pg.Vector2(3, 4)),
                      self.block_size, 0),
                Block(self.grid.place(self.pos, pg.Vector2(3, 3)),
                      self.block_size, 0),
                Block(self.grid.place(self.pos, pg.Vector2(3, 2)),
                      self.block_size, 0),
                Block(self.grid.place(self.pos, pg.Vector2(3, 1)),
                      self.block_size, 0),
            )

        )
        self.secs_blocks = (
            (Block(self.grid.place(self.pos, pg.Vector2(4, 4)), self.block_size, 0),
             Block(self.grid.place(self.pos, pg.Vector2(4, 3)), self.block_size, 0),
             Block(self.grid.place(self.pos, pg.Vector2(4, 2)), self.block_size, 0)
             ),
            (
                Block(self.grid.place(self.pos, pg.Vector2(5, 4)),
                      self.block_size, 0),
                Block(self.grid.place(self.pos, pg.Vector2(5, 3)),
                      self.block_size, 0),
                Block(self.grid.place(self.pos, pg.Vector2(5, 2)),
                      self.block_size, 0),
                Block(self.grid.place(self.pos, pg.Vector2(5, 1)),
                      self.block_size, 0),
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

    @classmethod
    def _resolve_state(cls, blocks, time):
        first_digit_bin = bin(int(time) // 10).split('b')[1][::-1]
        for i, digit_str in enumerate(first_digit_bin):
            blocks[0][i].state = int(digit_str)

        second_digit_bin = bin(int(time) % 10).split('b')[1][::-1]
        for i, digit_str in enumerate(second_digit_bin):
            blocks[1][i].state = int(digit_str)

    def _update_hours(self, time):
        hours = time.split(':')[0]
        self._resolve_state(self.hours_blocks, hours)
        self._resolve_state(self.hours_blocks, hours)

    def _update_mins(self, time):
        mins = time.split(':')[1]
        self._resolve_state(self.mins_blocks, mins)
        self._resolve_state(self.mins_blocks, mins)

    def _update_secs(self, time):
        secs = time.split(':')[2]
        self._resolve_state(self.secs_blocks, secs)
        self._resolve_state(self.secs_blocks, secs)

    def update(self):
        for block in self.blocks:
            block.state = 0
        time = datetime.now().strftime('%H:%M:%S')
        self._update_hours(time)
        self._update_mins(time)
        self._update_secs(time)
