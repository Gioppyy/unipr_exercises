while (n := int(input("Inserisci un numero di un carattere unicode (0 for exit): "))) != 0: print(f"Carattere Unicode N.{n}: {chr(n)}" if 0 <= n <= 1114111 else "Numero inserito non valido.")