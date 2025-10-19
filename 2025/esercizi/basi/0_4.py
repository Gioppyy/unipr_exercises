an, mn, gn = [int(x) for x in input("Inserisci anno, mese e giorni di nascita nel formato [anno mese giorno]: ").split(" ")]
ao, mo, go = [int(x) for x in input("Inserisci anno, mese e giorni di oggi nel formato [anno mese giorno]: ").split(" ")]

if (mo > mn) or (mo == mn and go >= gn):
    eta = ao - an
else:
    eta = ao - an - 1

print(f"Hai {eta} anni.")
