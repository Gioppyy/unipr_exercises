import g2d, random, math

sizex, sizey = 500, 500
finished = False

def gen_circle():
    r, g, b = [random.randint(1, 255) for _ in range(3)]
    x, y = [random.randint(0, 500) for _ in range(2)]
    g2d.set_color((r, g, b))
    g2d.draw_circle((x,y), 20)

    return x, y

def distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

def tick():
    global finished

    if not finished:
        xc,yc = gen_circle()
        if distance((sizex//2, sizey//2), (xc, yc)) < 20:
            print("Generazione finita")
            finished = True

def main():
    global g2d

    g2d.init_canvas((sizex, sizey))
    g2d.set_color((255,0,0))
    g2d.draw_circle((sizex//2, sizey//2), 5)
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()