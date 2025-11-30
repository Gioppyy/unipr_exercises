from math import sqrt
import random
import g2d

def init_colors():
    colors = []
    with open("colors.txt", "r") as f:
        for l in f.readlines():
            colors.append([int(x) for x in l.strip().split(",")])
    return colors

def rec_circles(p: g2d.Point, r: float, deep: int, colors: list):
    if deep == 0:
        return
    if r <= 5:
        return

    g2d.set_color(colors[deep % len(colors)])
    g2d.draw_circle(p, r)

    x, y = p
    positions = [(x+r, y+r), (x-r, y-r), (x+r, y-r), (x-r, y+r)]
    for pos in positions:
        rec_circles(pos, r * 0.42, deep-1, colors)

def main():
    g2d.init_canvas((500, 500))

    colors = init_colors()

    x = int(g2d.prompt("x? "))
    y = int(g2d.prompt("y? "))
    r = float(g2d.prompt("r? "))
    deep = int(g2d.prompt("deep? "))

    rec_circles((x,y), r, deep, colors)
    g2d.main_loop()

if __name__ == "__main__":
    main()
