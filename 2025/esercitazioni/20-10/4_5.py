from string import ascii_lowercase
from random import choice

def add_letter(st: str) -> str:
    return st + choice(ascii_lowercase)

def main():
    n = int(input("inserisci un n: "))
    st = ""
    for _ in range(n):
        st = add_letter(st)
    print(st)

if __name__ == "__main__":
    main()
