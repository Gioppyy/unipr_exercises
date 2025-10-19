from math import sqrt

class Quadratico:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def predict(self, x, y):
        return self._a*x + self._b * y + self._c
