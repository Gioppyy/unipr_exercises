from math import sqrt

class Quadratico:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def predict(self, x):
        return self._a*(x**2) + self._b * x + self._c
