def pow(x, n):
    if n == 0:
        return 1
    else:
      return x * pow(x, n-1)

x = int(input("Inserisci un numero: "))
n = int(input("Inserisci un esponente: "))
print(pow(x, n))
