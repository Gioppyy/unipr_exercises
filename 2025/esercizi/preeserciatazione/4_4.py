import g2d
from random import randrange

W, H = 400, 400

g2d.init_canvas((W, H))

n = int(g2d.prompt("n? "))
d = H / (n + 1)
r = d / 2

for i in range(n):
    for j in range(i+1):
        pos_0 = W / 2 - i * r

        pos_x = 2 * r * j + pos_0
        pos_y = 2 * r * i + r

        color = (randrange(256), randrange(256), randrange(256))
        g2d.set_color(color)
        g2d.draw_circle((pos_x, pos_y), r)

g2d.set_color(color)
g2d.draw_circle((W/2, r*2 * n + r), r)

g2d.main_loop()
