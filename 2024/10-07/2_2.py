import math

def heron(a: float, b: float, c: float) -> float:
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Un valore inserito non è valido.")

    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("I lati inseriti non formano un triangolo valido.")

    s = (a + b + c)/2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def main():
    try:
        a = float(input("Inserisci il lato A: "))
        b = float(input("Inserisci il lato B: "))
        c = float(input("Inserisci il lato C: "))

        print(heron(a, b, c))

    except ValueError as e:
        print(f"Errore! {e}")

if __name__ == "__main__":
    main()

