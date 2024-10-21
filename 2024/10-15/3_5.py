a = list()
while((n := int(input("Inserisci un numero (0 FOR EXIT): "))) != 0):
    a.append(n)

m = sum(a) / len(a)
print(f"μ: {m}")
print(f"var(x): {(sum([(x-m)**2 for x in a]) / len(a)):.2f}")