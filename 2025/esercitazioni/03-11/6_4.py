from math import dist
import g2d
import random

positions = []
finished = True

def distance(p1, p2):
    return abs(dist(p1, p2))

def tick():
    global finished

    if not finished:
        return

    r, g, b = [random.randint(0,255) for _ in range(3)]
    x, y = [random.randint(0,500) for _ in range(2)]
    g2d.set_color((r,g,b))
    g2d.draw_rect((x, y), (20, 20))
    for p in positions:
        if distance(p, (x, y)) <= 20:
            finished = False
            return
    positions.append((x, y))

def main():
    g2d.init_canvas((500, 500))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
