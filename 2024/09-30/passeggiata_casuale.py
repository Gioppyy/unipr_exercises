import g2d, random

sizex, sizey = 500,  500
x, y = 0, 0

n = int(input("Inserisci quanti passi fare: "))
while n > 50:
    n = int(input("Inserisci quanti passi fare: "))

for i in range(n):
    r = random.randint(0, 3)
    if r == 0: y -= 10
    elif r == 1: x += 10
    elif r == 2: y += 10
    else: x-= 10
    print(f"Passo N. {i+1} | r = {r}| coord: ({x}, {y})")

print(f"Coordinate finali: ({x}, {y})")
print(f"Distanza di Manhattan: {abs(x) + abs(y)}")