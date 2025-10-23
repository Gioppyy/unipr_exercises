import g2d

ARENA_W, ARENA_H = 500, 500

def draw_figure(centro: g2d.Point, raggio: int, n: int) -> int:
    for i in range(n, 0, -1):
        color = int(255 * (n - i) / n)
        g2d.set_color((color, color, color))
        g2d.draw_circle(centro, raggio * (i/n))

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))

    n = int(g2d.prompt("Inserisci quanti cerchi vuoi: "))
    r = ARENA_W/n/2
    for i in range(n):
        draw_figure((r + r*i*2, 250), r, n)

    g2d.main_loop()
    pass

if __name__ == "__main__":
    main()
