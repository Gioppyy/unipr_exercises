import g2d

g2d.init_canvas((500, 500))

def inp() -> int:
    try:
        r = int(g2d.prompt("Inserisci il tuo anno di nascita!"))
        return r
    except:
        return -1

def main():
    while( (anno := inp()) == -1):
        g2d.alert("Anno inserito non valido! riprova.")

    if anno % 12 == 8:
        print("Sei nato nell'anno del drago!")
    else:
        print("NON sei nato nell'anno del drago!")


if __name__ == "__main__":
    main()
