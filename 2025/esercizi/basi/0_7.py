import g2d
from random import randint

n = 0
max_q = 0
lato = 0

g2d.init_canvas((500, 500))

def inp() -> int:
    try:
        r = int(g2d.prompt("Inserisci un numero di quadrati!"))
        return r
    except:
        return -1


def tick():
    global n, lato

    if n < max_q:
        r,g,b = [randint(0, 255) for _ in range(3)]
        g2d.set_color((r, g, b))
        g2d.draw_rect((n*lato,n*lato), (lato, lato))
        n += 1
    pass

def main():
    global max_q, lato
    while( (r := inp()) == -1):
        g2d.alert("Anno inserito non valido! riprova.")

    lato = 500/r
    max_q = r
    g2d.main_loop(tick)


if __name__ == "__main__":
    main()
