#!/usr/bin/env python3
from random import randint
import g2d

x1, y1, dx1, dy1 = 200, 200, 2, 0
ARENA_W, ARENA_H, BALL_W, BALL_H = 400, 400, 20, 20

class RandomWalker:
    def __init__(self, x0: int, y0: int):
        self._x = x0
        self._y = y0

        if self._x % 2 != 0:
            self._x += 1
        if self._y % 2 != 0:
            self._y += 1

        self._dx, self._dy = 4, 4

    def move(self):
        if not 0 <= self._x + self._dx <= ARENA_W - BALL_W:
            self._dx = -self._dx
        if not 0 <= self._y + self._dy <= ARENA_H - BALL_H:
            self._dy = -self._dy
        self._x += self._dx
        self._y += self._dy

        if self._x % 20 == 0 and self._y % 20 == 0:
            self.get_random_dir()

    def pos(self) -> (int, int):
        return self._x, self._y

    def get_random_dir(self):
        direzioni = [d for d in [(0,2), (0,-2), (2,0), (-2,0)] if d != (-self._dx, -self._dy)]
        self._dx, self._dy = direzioni[randint(0, len(direzioni)-1)]

def tick():
    g2d.clear_canvas()
    g2d.draw_rect(b1.pos(), (20, 20))
    b1.move()

def main():
    global b1, g2d
    import g2d
    b1 = RandomWalker(140, 180)

    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
