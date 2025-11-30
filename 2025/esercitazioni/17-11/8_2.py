import g2d

def main():
    g2d.init_canvas((500, 500))

    colors = []
    with open("colors.txt", "r") as f:
        for l in f.readlines():
            colors.append([int(x) for x in l.strip().split(",")])

    n = int(g2d.prompt("n? "))
    for i in range(0, n):
        g2d.set_color(colors[i % len(colors)])
        g2d.draw_circle((250, 250), 200/(i+1))

    g2d.main_loop()

if __name__ == "__main__":
    main()
