class Person:
    def __init__(self, nome, cognome, anno, mese, giorno):
        self._nome = nome
        self._cognome = cognome
        self._anno = anno
        self._mese = mese
        self._giorno = giorno

    def age(self, oggi: list) -> bool:
        ao, mo, go = oggi

        if (mo > self._mese) or (mo == self._mese and go >= self._giorno):
            eta = ao - self._anno
        else:
            eta = ao - self._anno - 1

        self.describe(eta)

    def describe(self, eta):
        print(f"Sono {self._nome} {self._cognome}, ho {eta} anni e dunque {'non ' if eta < 18 else ''}sono maggiorenne")


def main():
    persone = []
    for i in range(3):
        nome = input("Inserisci nome: ")
        cognome = input("Inserisci cognome: ")
        an, mn, gn = [int(x) for x in input("Inserisci anno, mese e giorni di nascita nel formato [anno mese giorno]: ").split(" ")]

        p = Person(nome, cognome, an, mn, gn)
        persone.append(p)

    date = []
    while True:
        try:
            data = [int(x) for x in input("Inserisci anno, mese e giorni di oggi nel formato [anno mese giorno]: ").split(" ")]
            date.append(data)
        except:
            break

    for d in date:
        for p in persone:
            p.age(d)

if __name__ == "__main__":
    main()
