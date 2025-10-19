def inp() -> int:
    try:
        r = int(input("Inserisci un numero maggiore di 0: "))
        return r
    except:
        return -1

def main():
    while((n := inp()) == -1 or n <= 0):
        print("Numero inserito non valido! riprova.")

    tot = 0
    for k in range(n):
        tot += 2**k
    print(f"Totale somma di potenze: {tot}")

    gauss = 2**n - 1
    print(f"Somma calcolata con formula: {gauss}")

    print("Risultato corretto!" if tot == gauss else "Risultato non corretto!")

if __name__ == "__main__":
    main()
