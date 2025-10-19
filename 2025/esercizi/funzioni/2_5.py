def generate_group(st: str) -> list:
    if len(set(st)) != len(st):
        raise ValueError("L'alfabeto contiene caratteri ripetuti")

    ris = []

    for c1 in st:
        for c2 in st:
            for c3 in st:
                ris.append(c1 + c2 + c3)

    return ris

def main():
    print(generate_group(input("Inserisci un vocabolario: ")))

main()
