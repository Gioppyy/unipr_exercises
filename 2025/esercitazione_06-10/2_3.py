from random import randint
import g2d

g2d.init_canvas((500, 500))

n = 0
max_c = 0
start = 0
end = 0

def inp() -> int:
    try:
        r = int(g2d.prompt("Inserisci il numero di cerchi: "))
        return r
    except:
        return -1

def tick():
    global n, lato, start, start, end, end

    if n < max_c:
        n += 1
        r,g,b = [randint(0, 255) for _ in range(3)]
        g2d.set_color((r, g, b))

        mx = (end[0]-start[0]) / max_c - 1
        my = (end[1]-start[1]) / max_c - 1

        x = mx * n + start[0]
        y = my * n + start[1]
        g2d.draw_circle((x,y), 5)

def main():
    global max_c, start, end
    while( (n := inp()) == -1):
        g2d.alert("Numero inserito non valido! riprova.")
    max_c = n

    x1 = int(g2d.prompt("Inserisci x1: "))
    y1 = int(g2d.prompt("Inserisci y1: "))
    x2 = int(g2d.prompt("Inserisci x2: "))
    y2 = int(g2d.prompt("Inserisci y2: "))

    start = (x1, y1)
    end = (x2, y2)


    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
