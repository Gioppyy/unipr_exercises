import random

def main():
    w = int(input("w? "))
    h = int(input("h? "))
    n = int(input("n? "))

    game = []
    for i in range(h):
        game.append([0]*w)

    while n > 0:
        x = random.randint(0, w-1)
        y = random.randint(0, h-1)
        if game[y][x] == 0:
            game[y][x] = 1
            n -= 1

    print("DEBUG Matrice")
    for row in game:
        print(row)

    while (s := input("coords in formato: 'x y'? ")) != "":
        x, y = [int(n) for n in s.split(" ")]
        if x < w and y < h and x >= 0 and y >= 0:
            if game[y][x] == 1:
                print("Hai preso una bomba!")
            else:
                count = 0
                for i in range(max(0, y-1), min(h, y+2)):
                    for j in range(max(0, x-1), min(w, x+2)):
                        if (i != y or j != x) and game[i][j] == 1:
                            count += 1
            print(f"Numero di '1' vicini alla posizione ({x}, {y}): {count}")
        else:
            print("Coordinate non valide")

if __name__ == "__main__":
    main()
