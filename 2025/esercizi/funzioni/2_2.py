from math import pi

def ellipse_area(a: float, b: float) -> float:
    return pi * a * b

def main():
    a = float(input("Inserisci il semiasse a: "))
    b = float(input("Inserisci il semiasse b: "))
    print(ellipse_area(a, b))

main()
