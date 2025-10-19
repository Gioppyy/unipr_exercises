#!/usr/bin/env python3
from random import randint
import g2d

x1, y1, dx1, dy1 = 200, 200, 2, 0
ARENA_W, ARENA_H, BALL_W, BALL_H = 400, 400, 20, 20

def move_ball(x: int, y: int,
              dx: int, dy: int) -> tuple[int, int, int, int]:
    if not 0 <= x + dx <= ARENA_W - BALL_H:
        dx = -dx
    if not 0 <= y + dy <= ARENA_H - BALL_H:
        dy = -dy
    x += dx
    y += dy
    return (x, y, dx, dy)

def get_random_dir() -> tuple[int, int]:
    n = randint(0, 3)
    match n:
        case 0:
            return (0, 2)
        case 1:
            return (0, -2)
        case 2:
            return (2, 0)
        case 3:
            return (-2, 0)
def tick():
    global x1, y1, dx1, dy1, cooldown
    g2d.clear_canvas()
    g2d.draw_image("ball.png", (x1, y1))

    if x1 % 20 == 0 and y1 % 20 == 0:
        dx1, dy1 = get_random_dir()
    print(dx1, dy1)
    x1, y1, dx1, dy1 = move_ball(x1, y1, dx1, dy1)

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
