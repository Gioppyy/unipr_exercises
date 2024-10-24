# https://tomamic.github.io/esercizi-2024.html#/33

from math import e, exp

class CurveEsponenziali:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
    
    def estimate(self, x):
        return self._a * exp(self._b * x) + self._c
    
def main():
    a, b, c = [int(i) for i in input("Inserire i tre coefficenti separati da virgole (Es. 1,2,3): ").split(",")]
    curva = CurveEsponenziali(a, b, c)
    while( (x := input("Inserisci un valore di X (ENTER for exit): ")) != ""):
        print(curva.estimate(int(x)))

