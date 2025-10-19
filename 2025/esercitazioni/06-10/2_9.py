def count_groups(text: str) -> tuple[int, int]:
    g1, g2 = 0, 0
    for c in text.lower():
        if 'a' <= c <= 'm': g1 += 1
        elif 'n' <= c <= 'z': g2 += 1
    return (g1, g2)

def main():
    while ((t := input("Inserisci un testo [INVIO for EXIT]: ")) != ""):
        print(count_groups(t))
    print("Conteggio terminato!")
if __name__ == "__main__":
    main()
