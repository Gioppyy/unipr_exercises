from random import choice

H,W = 24, 4

letters = list(map(chr, range(31, 127)))

for y in range(W):
    for x in range(H):
        end_ = "\n" if x == H-1 else ""
        print(letters[x*W + y], end=end_)

print()

for y in range(W):
    for x in range(H):
        end_ = "\n" if x == H-1 else ""
        print(letters[y*H + x], end=end_)
