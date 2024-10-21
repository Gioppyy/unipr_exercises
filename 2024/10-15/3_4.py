def slope(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]

    if dx == 0:
        raise ValueError("I punti sono allineati verticalmente!")
    
    return dy / dx


def main():
    p1 = tuple(int(x) for x in input("Inserisci le coordinate del Primo punto separati da virgole (Es. 1,2): ").split(","))
    p2 = tuple(int(x) for x in input("Inserisci le coordinate del Secondo punto separati da virgole (Es. 1,2): ").split(","))

    try:
        print(f"{slope(p1,p2):.2f}")
    except ValueError as e: 
        print(e)

if __name__ == "__main__":
    main()