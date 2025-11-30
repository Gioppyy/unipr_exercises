import g2d

def triangoli(pos, w, h, n):
    if n == 0:
        return
    if w < 5 or h < 5:
        return

    x, y = pos
    g2d.set_color((0,0,0))
    g2d.draw_rect((x,y), (w,h))
    g2d.set_color((255, 255, 255))
    g2d.draw_rect((x,y), (w/2,h/2))

    w = w/2
    h = h/2
    pos = [(x+w, y), (x, y+h), (x+w, y+h)]
    for i in range(3):
        triangoli(pos[i], w, h, n-1)

def main():
    g2d.init_canvas((500, 500))

    n = int(g2d.prompt("n? "))
    triangoli((250, 250), 200, 200, n)

    g2d.main_loop()

if __name__ == "__main__":
    main()
