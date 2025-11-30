from random import randint

def main():
    w = int(input("w? "))
    h = int(input("h? "))
    m = [[0] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            m[i][j] = randint(0, 9)
    print(f"matrice: ", m)

    colons = []
    for j in range(w):
        col = []
        for i in range(h):
            col.append(int(m[i][j]))
        colons.append(col)

    nums = colons[0]
    for col in colons[1::]:
        print(col)
        for i, n in enumerate(nums):
            if not n in col:
                del nums[i]
    print("numeri in tutte le colonne", nums)
if __name__ == "__main__":
    main()
