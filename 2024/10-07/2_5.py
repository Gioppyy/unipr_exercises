import g2d, random

sizex, sizey = 500, 500
ra = 200

g2d.init_canvas((sizex, sizey))
r, g, b = [random.randint(1, 255) for _ in range(3)]
g2d.set_color((r, g, b))
g2d.draw_circle((sizex//2, sizey//2), ra)

while ra > 10:
    r, g, b = [random.randint(1, 255) for _ in range(3)]
    ra = random.randint(10, ra)
    g2d.set_color((r, g, b))
    g2d.draw_circle((sizex//2, sizey//2), ra)

g2d.main_loop()