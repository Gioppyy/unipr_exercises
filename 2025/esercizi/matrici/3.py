from random import randrange
from math import sin, cos

def spiral_fill(h, w):
    mtx = [[0]*w for _ in range(h)]

    dirs = [(0,1), (1,0), (0,-1), (-1,0)]
    x, y = 0, 0
    d = 0

    for num in range(1, h*w + 1):
        mtx[x][y] = num
        nx = x + dirs[d][0]
        ny = y + dirs[d][1]

        if nx < 0 or nx >= h or ny < 0 or ny >= w or mtx[nx][ny] != 0:
            d = (d + 1) % 4
            nx = x + dirs[d][0]
            ny = y + dirs[d][1]

        x, y = nx, ny

    return mtx


def main():
    h = int(input("Altezza: "))
    w = int(input("Larghezza: "))

    mtx = spiral_fill(h, w)
    for row in mtx:
        print(row)

if __name__ == "__main__":
    main()
