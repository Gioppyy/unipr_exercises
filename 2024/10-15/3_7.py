import g2d, random

n = int(input("Inserisci un numero intero: "))

g2d.init_canvas((500, 500))

if n > 0:
    pos = (0, 0)
    for i in range(n):
        for j in range(0,i+1):
            r, g, b = [random.randint(0,255) for x in range(3)]
            g2d.set_color((r, g, b))
            g2d.draw_circle((pos[0]+40, pos[1]+60), 25)
            pos = (pos[0]+50, pos[1])
        pos = (0, pos[1] + 50)

g2d.main_loop()
