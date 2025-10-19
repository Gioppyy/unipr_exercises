from math import pi

def inp() -> int:
    try:
        r = int(input("Inserisci un raggio: "))
        return r
    except:
        return -1

def circumference(raggio: float) -> float:
    if raggio < 0:
        raise ValueError("Raggio negativo!")
    return 2*pi*raggio

def main():
    while( (r := inp()) == -1):
        print("Raggio inserito non valido! riprova.")
    print(f"Circonferenza: {circumference(r):.2f}")

if __name__ == "__main__":
    main()
