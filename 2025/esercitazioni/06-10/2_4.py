from random import randint
import g2d

g2d.init_canvas((500, 500))

n = 0
max_c = 0
start = 0
end = 0
start_c = (0,0,0)
end_c = (0,0,0)

def inp() -> int:
    try:
        r = int(g2d.prompt("Inserisci il numero di cerchi: "))
        return r
    except:
        return -1

def inp_color() -> g2d.Color:
    try:
        c = [int(n) for n in g2d.prompt("Inserisci un colore rgb separando i numeri da spazi: ").split(" ")]
        return c
    except:
        return None

def tick():
    global n, lato, start, start, end, end

    if n < max_c:
        n += 1

        r = start_c[0]+(end_c[0]-start_c[0]) * n // (max_c-1)
        g = start_c[1]+(end_c[1]-start_c[1]) * n // (max_c-1)
        b = start_c[2]+(end_c[2]-start_c[2]) * n // (max_c-1)

        g2d.set_color((r, g, b))

        mx = (end[0]-start[0]) / max_c - 1
        my = (end[1]-start[1]) / max_c - 1

        x = mx * n + start[0]
        y = my * n + start[1]
        g2d.draw_circle((x,y), 5)

def main():
    global max_c, start, end, start_c, end_c
    while( (n := inp()) == -1):
        g2d.alert("Numero inserito non valido! riprova.")
    max_c = n

    x1 = int(g2d.prompt("Inserisci x1: "))
    y1 = int(g2d.prompt("Inserisci y1: "))
    x2 = int(g2d.prompt("Inserisci x2: "))
    y2 = int(g2d.prompt("Inserisci y2: "))

    while( (c := inp_color()) == None):
        g2d.alert("Colore inserito non valido! riprova.")
    start_c = c

    while( (c := inp_color()) == None):
        g2d.alert("Colore inserito non valido! riprova.")
    end_c = c

    start = (x1, y1)
    end = (x2, y2)


    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
