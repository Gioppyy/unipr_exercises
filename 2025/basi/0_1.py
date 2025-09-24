import g2d
from random import randint
from math import pi

g2d.init_canvas((500, 500))

def inp() -> int:
    try:
        r = int(g2d.prompt("Inserisci il raggio!"))
        return r
    except:
        return -1

def main():
    global max_q, lato
    while( (r := inp()) == -1 or r > 200):
        g2d.alert("Numero inserito non valido! riprova.")

    g2d.set_color((38, 210, 235))
    g2d.draw_circle((250, 250), r)

    g2d.set_color((0, 0, 0))
    g2d.draw_text(f"A = {(pi * (r**2)):.2f}", (250, 230-r), 30)
    g2d.draw_text(f"C = {(r*pi*2):.2f}", (250, 270+r), 30)

    g2d.main_loop()

if __name__ == "__main__":
    main()
