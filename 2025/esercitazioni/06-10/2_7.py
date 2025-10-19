#!/usr/bin/env python3
from random import randint
from math import sin, pi
import g2d

x1, y1, dx1 = 200, 200, 2
ARENA_W, ARENA_H, BALL_W, BALL_H = 400, 400, 20, 20
AMPIEZZA, PERIODO = 10, 80
def move_ball(x: int, y: int,
              dx: int) -> tuple[int, int, int]:
    if not 0 <= x + dx:
        dx = -dx
    if x+dx >= ARENA_W + BALL_H:
        x = 0
    x += dx
    return (x, y, dx)

def tick():
    global x1, y1, dx1, dy1, cooldown
    g2d.clear_canvas()
    g2d.draw_image("ball.png", (x1, y1))

    y1 = y1 + AMPIEZZA * sin(x1 * 2*pi / PERIODO)
    x1, y1, dx1 = move_ball(x1, y1, dx1)

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
