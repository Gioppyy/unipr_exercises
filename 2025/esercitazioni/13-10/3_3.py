import random
ARENA_W, ARENA_H, BALL_W, BALL_H = 480, 360, 20, 20

class Ball:
    def __init__(self, x0: int, y0: int):
        self._x = x0
        self._y = y0
        self._dx, self._dy = 4, 4
        self._color = [random.randint(0,255) for _ in range(3)]

    def move(self):
        if not 0 <= self._x + self._dx <= ARENA_W - BALL_W:
            self._dx = -self._dx
            self.set_color()
        if not 0 <= self._y + self._dy <= ARENA_H - BALL_H:
            self._dy = -self._dy
            self.set_color()
        self._x += self._dx
        self._y += self._dy

    def pos(self) -> (int, int):
        return self._x, self._y

    def set_color(self):
        self._color = [random.randint(0,255) for _ in range(3)]

    def color(self) -> int:
        return self._color


def tick():
    g2d.clear_canvas()

    g2d.set_color(b1.color())
    g2d.draw_rect(b1.pos(), (20, 20))

    g2d.set_color(b2.color())
    g2d.draw_rect(b2.pos(), (20, 20))

    g2d.set_color(b3.color())
    g2d.draw_rect(b3.pos(), (20, 20))

    b1.move()
    b2.move()
    b3.move()

def main():
    global b1, b2, b3, g2d
    import g2d
    b1 = Ball(140, 180)
    b2 = Ball(180, 140)
    b3 = Ball(220, 100)

    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
