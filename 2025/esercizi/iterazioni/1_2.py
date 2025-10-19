"""
Chiedere all'utente un numero n
In un canvas L×L
, con L=500
 predefinito
Disegnare una fila orizzontale di n
 cerchi
Tutti di uguale dimensione
Coprono tutta la larghezza del canvas
Il colore varia gradualmente dal nero fino al blu saturo
Da sinistra verso destra
"""

import g2d
from random import randint

n = 0
max_s = 0
r = 0

g2d.init_canvas((500, 500))

def inp() -> int:
    try:
        r = int(g2d.prompt("Inserisci un numero di cerchi!"))
        return r
    except:
        return -1

def tick():
    global n, max_s, r

    if n < max_s:
        g2d.set_color((0,0, int(255 * n / (max_s - 1))))
        g2d.draw_circle(( r + n * 2 * r , 250 ), r)
        n += 1
    pass

def main():
    global max_s, r
    while( (s := inp()) == -1):
        g2d.alert("Numero inserito non valido! riprova.")

    r = 500/(s*2)
    max_s = s
    g2d.main_loop(tick)


if __name__ == "__main__":
    main()
