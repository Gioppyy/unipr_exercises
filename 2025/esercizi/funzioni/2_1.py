def cels_to_fahr(celsius: float) -> float:
    return celsius * 1.8 + 32

def main():
    print(cels_to_fahr(float(input("Inserisci una temperatura in celsius: "))))

main()
