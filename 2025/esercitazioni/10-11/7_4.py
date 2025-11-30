from math import sqrt
import random
import g2d

def rec_circles(p: g2d.Point, r: float):
    if r <= 5:
        return

    g2d.set_color((0,0,0))
    g2d.draw_circle(p, r)

    x, y = p
    rec_circles((x+r,y+r), r * 0.42)
    rec_circles((x-r,y-r), r * 0.42)
    rec_circles((x+r,y-r), r * 0.42)
    rec_circles((x-r,y+r), r * 0.42)

def main():
    g2d.init_canvas((500, 500))
    x = int(g2d.prompt("x? "))
    y = int(g2d.prompt("y? "))
    r = float(g2d.prompt("r? "))

    rec_circles((x,y), r)
    g2d.main_loop()

if __name__ == "__main__":
    main()
