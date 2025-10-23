from math import cos, sin, pi
from random import uniform
import g2d

ARENA_W, ARENA_H = 500, 500

def randline(p1: g2d.Point):
    a = uniform(0, 2 * pi)

    x = p1[0] + 100 * cos(a)
    y = p1[1] + 100 * sin(a)

    g2d.draw_line(p1, (x, y), 3)

    return (x, y)

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))

    n = int(g2d.prompt("Inserisci quante linee  vuoi: "))
    p = (250, 250)
    for i in range(n):
        p = randline(p)

    g2d.main_loop()

if __name__ == "__main__":
    main()
