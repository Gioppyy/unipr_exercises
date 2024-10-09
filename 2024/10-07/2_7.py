numbers = []
n = 1
while (n := int(input("Inserisci un numero da aggiungere alla lista (0 for exit): "))) != 0:
    numbers.append(n)

media = sum(numbers) / len(numbers)
meno = [n for n in numbers if n < media]
sopra = [n for n in numbers if n >= media]

print(f"Media: {media:4.2f}")
print(f"Numeri sotto la media: {meno}")
print(f"Numeri sopra la media: {sopra}")
