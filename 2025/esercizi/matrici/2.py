from random import randrange

def smooth(mtx: list) -> list:
    rows = len(mtx)
    cols = len(mtx[0])

    smoothed = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            total = mtx[i][j]
            count = 1

            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols:
                    total += mtx[ni][nj]
                    count += 1

            smoothed[i][j] = total // count

    return smoothed

def smooth2(mtx: list, rows: int, cols: int) -> list:
    smoothed = [0] * rows*cols

    for i in range(rows):
        for j in range(cols):
            total = mtx[i*cols + j]
            count = 1

            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols:
                    total += mtx[ni*cols + nj]
                    count += 1

            smoothed[i*cols + j] = total // count

    return smoothed

def main():
    h, w = 4, 3
    mtx = [[randrange(h*w) for _ in range(w)] for _ in range(h)]
    mtx2 = [randrange(h*w) for _ in range(w*h)]
    print(smooth(mtx))
    print(smooth2(mtx2, h, w))

if __name__ == "__main__":
    main()
