import g2d, random

sizex, sizey = 200, 200
x, y = sizex//2, sizey//2
steps = 0
i = 0
last = (x, y)

def draw_cross(x, y):
    c = min((steps-i) * (255 // 50), 255)
    if c == 255: c = 245                    # Impedisco che la croce diventi bianca
    g2d.set_color((c,c,c))                  # Setto il colore casuale
    g2d.draw_line((x+4, y), (x-3, y), 2)    # Disegno la linea orizzontale
    g2d.draw_line((x, y+4), (x, y-3), 2)    # Disegno la linea verticale

def apply_step_condition(xc, yc, r):
    if r == 0: yc -= 10
    elif r == 1: xc += 10
    elif r == 2: yc += 10
    else: xc -= 10

    # Faccio si che se le croci escono da un lato le fa ripartire dal lato opposto
    if   xc >= sizex:     xc = 0
    elif xc <= 0:       xc = sizex
    elif yc >= sizey:   yc = 0
    elif yc <= 0:       yc = sizey

    return (xc, yc)

def tick():
    global x, y, i, last
    if i > 0:
        while True:
            r = random.randint(0, 3)
            np = apply_step_condition(x, y, r)

            if np != last:
                last = (x, y)
                x = np[0]
                y = np[1]
                break

        draw_cross(x, y)
        i -= 1

def main():
    global steps, i
    
    steps = int(input("Inserisci quanti passi fare: "))
    while steps > 50:
        steps = int(input("Inserisci quanti passi fare: "))
    
    i = steps
    g2d.init_canvas((sizex, sizey))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()