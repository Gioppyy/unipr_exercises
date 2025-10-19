from random import randint

a,b,c = [randint(1, 6) for _ in range(3)]

print(f"Numeri estratti {a = }, {b = }, {c = }")

if a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
else:
    print(c)

#print(min([a, b, c]))
