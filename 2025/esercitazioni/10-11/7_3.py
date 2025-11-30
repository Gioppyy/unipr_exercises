from random import randrange

def main():
    w = int(input("w? "))
    h = int(input("h? "))

    l = [chr(randrange(97, 122)) for _ in range(w*h)]

    for i, n in enumerate(l):
        print(n, end="," if i % w != w-1 else "\n")

    while (c := input("Inserisci un carattere da cercare: ")) != "":
        print("appare in totale: " + l.count(c))

if __name__ == "__main__":
    main()
