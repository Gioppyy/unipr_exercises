with open("resistenze.txt", "r") as f:
    lines = list(map(int, f.readlines()))

serie = sum(lines)

par=0
for l in lines:
    par += 1/l

print("in serie: ", serie)
print(f"in serie: {1/par:.2f}")

