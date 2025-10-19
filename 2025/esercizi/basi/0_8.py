import g2d
from random import randint

n = 0
max_s = 0

g2d.init_canvas((500, 500))

def inp() -> int:
    try:
        r = int(g2d.prompt("Inserisci un numero di segmenti!"))
        return r
    except:
        return -1

def tick():
    global n, max_s

    if n < max_s:
        x1, y1, x2, y2 = [randint(10, 490) for _ in range(4)]
        g2d.draw_line((x1, y1), (x2, y2))
        n += 1
    pass

def main():
    global max_s, lato
    while( (s := inp()) == -1):
        g2d.alert("Anno inserito non valido! riprova.")

    max_s = s
    g2d.set_color((0,0,0))
    g2d.main_loop(tick)


if __name__ == "__main__":
    main()
