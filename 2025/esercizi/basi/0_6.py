import g2d
from random import randint

g2d.init_canvas((500, 500))
n = 0
max_q = 0

def inp() -> int:
    try:
        r = int(g2d.prompt("Inserisci un numero di quadrati!"))
        return r
    except:
        return -1


def tick():
    global n

    if n < max_q:
        r,g,b = [randint(0, 255) for _ in range(3)]
        g2d.set_color((r, g, b))
        g2d.draw_rect((randint(0, 400), randint(0, 400)), (100, 100))
        n += 1
    pass

def main():
    global max_q
    while( (r := inp()) == -1):
        g2d.alert("Anno inserito non valido! riprova.")

    max_q = r
    g2d.main_loop(tick)


if __name__ == "__main__":
    main()
