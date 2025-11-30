from polar import move_around
import g2d

def albero_fratturale(pos, l, a):
    if l < 5:
        g2d.set_color((0, 240, 0))
        g2d.draw_line(pos, move_around(pos, l, 90 + a), 2)
        return

    g2d.set_color((101, 67, 33))
    end_pos = move_around(pos, l, 90 + a)
    g2d.draw_line(pos, end_pos, 3)

    new_l = l * 4/5
    albero_fratturale(end_pos, new_l, a - 30)
    albero_fratturale(end_pos, new_l, a + 30)

def main():
    g2d.init_canvas((500, 500))

    l = int(g2d.prompt("l? "))
    albero_fratturale((250, 400), l, 180)

    g2d.main_loop()

if __name__ == "__main__":
    main()
