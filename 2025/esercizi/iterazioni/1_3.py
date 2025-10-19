"""
Chiedere all'utente un numero n
In un canvas L×L
, con L=500
 predefinito
Disegnare n
 cerchi al centro del canvas
Diametro decrescente, da L
 fino a Ln
Colore da rosso (cerchio esterno) a nero
"""

import g2d
from random import randint

n = 0
max_s = 0

g2d.init_canvas((500, 500))

def inp() -> int:
    try:
        r = int(g2d.prompt("Inserisci un numero di cerchi!"))
        return r
    except:
        return -1

def tick():
    global n, max_s

    if n < max_s:
        r = int(255 * (1 - n / (max_s - 1))) if max_s > 1 else 255
        g2d.set_color((r,0,0))
        g2d.draw_circle((250, 250), 250/(n+1))
        n += 1
    pass

def main():
    global max_s
    while( (s := inp()) == -1):
        g2d.alert("Numero inserito non valido! riprova.")

    max_s = s
    g2d.main_loop(tick)


if __name__ == "__main__":
    main()
