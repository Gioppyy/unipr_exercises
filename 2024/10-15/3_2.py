class Parallelepipedo():
    def __init__(self, larghezza, altezza, profondita):
        self._larghezza = larghezza
        self._altezza = altezza
        self._profondita = profondita

    def superficie(self):
        return 2 * ((self._larghezza * self._altezza) + (self._larghezza * self._profondita) + (self._altezza * self._profondita))

    def volume(self):
        return (self._larghezza * self._altezza * self._profondita)

def main():
    larghezza = float(input("Inserisci la larghezza del parallelepipedo: "))   
    altezza = float(input("Inserisci la altezza del parallelepipedo: "))
    profondita = float(input("Inserisci la profondità del parallelepipedo: "))    

    parallelepipedo = Parallelepipedo(larghezza, altezza, profondita)
    print(f"Superficie: {parallelepipedo.superficie()}")
    print(f"Volume: {parallelepipedo.volume()}")

if __name__ == "__main__":
    main()