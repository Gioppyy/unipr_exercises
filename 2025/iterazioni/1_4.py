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
        r, g, b = [randint(0, 255) for _ in range(3)]
        g2d.set_color((r, g, b))

        passo = lato / 2
        x = int(n * passo)
        y = int(n * passo)

        g2d.draw_rect((x, y), (lato, lato))
        n += 1

def main():
    global max_q, lato
    while( (r := inp()) == -1):
        g2d.alert("Numero inserito non valido! riprova.")

    max_q = r
    lato = (2 * 500) / (max_q + 1)

    g2d.main_loop(tick)


if __name__ == "__main__":
    main()
