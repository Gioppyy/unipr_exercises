import g2d

n = int(input("Inserisci quanti quadrati vuoi: "))

g2d.init_canvas((500, 500))

smallest_side = 500 / n
squares = [(smallest_side * (n - i), (0, 0)) for i in range(n)]
colors = [(0, 0, 0) if i == 0 else (0, int((255 * i) / (n - 1)), 0) for i in range(n)]

for i in range(n):
    g2d.set_color(colors[i])
    side_length = squares[i][0]
    x = 500 - side_length - 10
    g2d.draw_rect((x, 10), (side_length, side_length))

g2d.main_loop()
