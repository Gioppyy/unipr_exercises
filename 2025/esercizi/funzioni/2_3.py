from math import pi

def triangle_perimeter (a: float, b: float, c: float) -> float:
    if (a + b) > c or a > (b + c):
        raise ValueError("Non è un triangolo")
    return a + b + c

def main():
    a = float(input("Inserisci il lato a: "))
    b = float(input("Inserisci il lato b: "))
    c = float(input("Inserisci il lato c: "))
    print(triangle_perimeter(a, b, c))

main()
