import g2d, random

sizex, sizey = 500, 500
n = 0

def draw_rect_with_shadow():
    r, g, b = [random.randint(1, 255) for _ in range(3)]
    x, y = [random.randint(0, 500) for _ in range(2)]
    w, h = [random.randint(20, 500) for _ in range(2)] # Inserisco un minimo di 20 pixel per evitare delle "righe"

    g2d.set_color((90,91,92))           # Setto il colore a grigio
    g2d.draw_rect((x+5, y+5), (w, h))   # Disegno l'ombra
    g2d.set_color((r,g,b))              # Setto il colore ad uno randomico
    g2d.draw_rect((x, y), (w, h))       # Disegno il rettangolo casuale

def tick():
    global n
    if n > 0 :
        draw_rect_with_shadow()
        n -= 1

def main(): 
    global n
    n = int(input("Inserisci quanti rettangoli vuoi: "))
    g2d.init_canvas((sizex, sizey))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
