def inp(i) -> int:
    try:
        r = int(input(f"Inserisci il numero n.{i+1} [1. w | 2. h]: "))
        return r
    except:
        return -99999999

def manhattan(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    for y in range(x2):
        for x in range(y2):
            distanza = abs(x - x1) + abs(y - y1)
            print(distanza, end=" ")
        print()

def main():

    p = []
    for i in range(2):
        while((n := inp(i)) == -99999999):
            print("Numero inserito non valido! riprova.")
        p.append(n)

    print("\nDistanza da {0, 0}:")
    manhattan((0, 0), (p[1], p[0]))

    print("\nDistanza da {0, h-1}:")
    manhattan((0, p[1]-1), (p[1], p[0]))



if __name__ == "__main__":
    main()
