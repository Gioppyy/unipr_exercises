def check_chars(s: str):
    z, u = 0, 0

    for c in s: 
        if c == "0": z += 1
        elif c == "1": u += 1

    return (z, u)

"""
Se volessimo contare gli 0 ed 1 dei bit in una frase
    def check_chars(s: str):
        z, u = 0, 0

        for c in s: 
            c = bin(ord(c))[2::]
            for b in c:
                if b == "0": z += 1
                elif b == "1": u += 1

        return (z, u)
"""

"""
Volendo possiamo usare le funzioni di python
    def check_chars(s: str):
        return (s.count("0"), s.count("1"))
"""

def main():
    while ((s := input("Inserisci un testo di cui contare gli 0 e gli 1 (ENTER for exit): ")) != ""):
        res = check_chars(s)
        print(f"Numero di 0: {res[0]}")
        print(f"Numero di 1: {res[1]}")

if __name__ == "__main__":
    main()