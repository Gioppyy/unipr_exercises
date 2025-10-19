def count_groups(st: str) -> tuple[int, int]:
    t1, t2 = 0, 0
    for c in st:
        if "a" <= c.lower() <= "m":
            t1 += 1
        if "n" <= c.lower() <= "z":
            t2 += 1
    return (t1, t2)

def main():
    print(count_groups(input("Inserisci una frase: ")))

main()
