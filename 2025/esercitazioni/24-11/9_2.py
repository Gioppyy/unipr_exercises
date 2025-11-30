def main():

    w, h = 0, 0
    with open("matrice.csv", "r") as f:
        lines = f.readlines()
        h = len(lines)

        m = [0] * h
        for i, l in enumerate(lines):
            row = l.strip().split(",")
            w = len(row)
            m[i] = row

    nm = [[0] * w for _ in range(h)]
    for j in range(w):
        col = []
        for i in range(h):
            col.append(int(m[i][j]))

        nmax = max(col)
        nmin = min(col)

        ncol = [(x - nmin) / (nmax - nmin) for x in col]
        for i in range(h):
            nm[i][j] = ncol[i]

    with open("matrice_normalizzata.csv", "w") as f:
        for i in range(h):
            line = ",".join(f"{nm[i][j]:.2f}" for j in range(w))
            f.write(line + "\n")

if __name__ == "__main__":
    main()
