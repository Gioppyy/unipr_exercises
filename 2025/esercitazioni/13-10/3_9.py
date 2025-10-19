#!/usr/bin/env python3
from random import randint
from math import sin, pi
import g2d

ARENA_W, ARENA_H, BALL_W, BALL_H = 400, 400, 20, 20
AMPIEZZA, PERIODO = 10, 120
SHOW_POS = (20, 0)
HIDE_POS = (20,20)

class OscillatingGhost:
    def __init__(self, x0: int, y0: int):
        self._x = x0
        self._y = y0
        self._dx = 4
        self._visible = True
        self._sprite = SHOW_POS

    def move(self):
        if not 0 <= self._x + self._dx:
            self._dx = -self._dx
        if self._x + self._dx >= ARENA_W + BALL_H:
            self._x = 0
            self._y = 200
        self._x += self._dx

        self._y = self._y + AMPIEZZA * sin(self._x * 2 * pi / PERIODO)

        if self._x % 20 == 0 and randint(1, 3) == 2:
            self._visible = not self._visible
            self._sprite = SHOW_POS if self._visible else HIDE_POS

    def pos(self) -> (int, int):
        return self._x, self._y

    def size(self) -> (int, int):
        return (20, 20)

    def sprite(self):
        return self._sprite

def tick():
    g2d.clear_canvas()
    g2d.draw_image("sprites.png", ghost.pos(), ghost.sprite(), ghost.size())

    ghost.move()

def main():
    global ghost

    g2d.init_canvas((ARENA_W, ARENA_H))
    ghost = OscillatingGhost(200, 200)

    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
