#!/usr/bin/env python3
import g2d

x1, y1, dx1 = 200, 200, 2
cooldown = 0
ARENA_W, ARENA_H, BALL_W, BALL_H = 400, 400, 20, 20

def move_ball(x: int, y: int,
              dx: int) -> tuple[int, int, int]:
    if not 0 <= x + dx <= ARENA_W - BALL_H:
        dx = -dx
    x += dx
    return (x, y, dx)

def tick():
    global x1, y1, dx1, cooldown
    g2d.clear_canvas()
    g2d.draw_image("ball.png", (x1, y1))

    if cooldown > 0:
        cooldown -= 1
        return

    if g2d.mouse_clicked():
        cooldown = 30
    else:
        x1, y1, dx1 = move_ball(x1, y1, dx1)

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
