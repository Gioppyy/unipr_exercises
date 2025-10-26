from g2d import Point
from actor import Actor, Arena
from random import choice, randrange, uniform
from math import cos, pi, sin

class Ghost(Actor):
    def __init__(self):
        a = uniform(0, 2 * pi)

        x = 350 * cos(a)
        y = 350 * sin(a)

        self._x, self._y = (x, y)
        self._start_x, self._start_y = (x, y)

        self._w, self._h = 20, 20
        self._visible = True

    def move(self, arena: Arena):
        aw, ah = arena.size()
        dx = choice([-4, 0, 4])
        dy = choice([-4, 0, 4])
        self._x = (self._x + dx) % aw
        self._y = (self._y + dy) % ah

        keys = arena.current_keys()
        if "h" in keys:
            self._x, self._y = self._start_x, self._start_y

    def pos(self) -> Point:
        return self._x, self._y

    def size(self) -> Point:
        return self._w, self._h

    def sprite(self) -> Point:
        if self._visible:
            return 20, 0
        return 20, 20

