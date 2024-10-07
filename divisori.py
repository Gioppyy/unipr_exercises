n = int(input("Inserisci un numero di cui vuoi sapere i divisori: "))
print(*[x for x in range(1, n+1) if n % x == 0])