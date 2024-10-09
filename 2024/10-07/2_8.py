def check_chars(s: str):
    z, u = 0

    for c in s: 
        if c == "0": z += 1
        elif c == "1": u += 1

    return (z, u)

def main():
    s = "a"
    while s != "":
        s = input("Inserisci una frase di cui vuoi sapere il numero di 0 e 1 (ENTER for exit): ")
        if s != "":
            res = check_chars(s)
            print(f"Numero di 0: {res[0]}")
            print(f"Numero di 1: {res[1]}")

if __name__ == "__main__":
    main()