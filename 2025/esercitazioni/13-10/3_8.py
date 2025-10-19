def count_chars(s: str) -> tuple[int, int]:
    p, d = 0, 0
    for c in s:
        if c.islower():
            if ord(c) % 2 == 0:
                p += 1
            else:
                d += 1
    return (p, d)

def main():
    p, d = 0, 0
    while ((s := input("Inserisci una stringa [ENTER for EXIT]: ")) != ""):
        p1, d1 = count_chars(s)
        p += p1
        d += d1
    print(f"Ci sono {p} minuscole pari")
    print(f"Ci sono {d} minuscole dipari")

if __name__ == "__main__":
    main()
