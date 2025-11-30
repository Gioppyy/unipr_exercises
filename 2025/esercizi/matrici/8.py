fn = input("nome file? ")


with open(fn) as f:
    lines = list(map(float, f.readlines()))

print("min: ", min(lines))
print("max: ", max(lines))
