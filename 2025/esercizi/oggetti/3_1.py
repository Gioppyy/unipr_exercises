from math import pi, sqrt

class Ellisse:
    def __init__(self, a: int, b: int):
        self._a = a
        self._b = b

    def area(self):
        return pi * self._a * self._b

    def fuoco(self):
        return sqrt(self._a**2, self._b**2)
