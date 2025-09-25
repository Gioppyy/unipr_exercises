from random import randint

def inp() -> int:
    try:
        r = int(input("Prova ad indovinare il numero tra 0 e 90: "))
        return r
    except:
        return -1

def main():
    guess = randint(0, 90)

    n = 0
    while n != guess:
        while((n := inp()) == -1):
            print("❌  Numero inserito non valido! riprova.")

        if n < guess:
            print("⬆️  Numero troppo basso!")
        elif n > guess:
            print("⬇️  Numero troppo alto!")
    print("🎉 Numero giusto!")


if __name__ == "__main__":
    main()
