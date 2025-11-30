from random import randint

def main():
    w = int(input("w? "))
    h = int(input("h? "))

    nums = [x for x in range(1, (h*w)+1)]
    m = [[0] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            m[i][j] = nums.pop(randint(0, len(nums)-1))

    with open("matrice.csv", "w") as f:
        for l in m:
                f.write(",".join(str(x) for x in l) + "\n")
    print(m)

if __name__ == "__main__":
    main()
