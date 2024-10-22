import math

sq = lambda delta : math.sqrt(delta)

def solve_quadratic(a, b, c):
    d = b**2 - 4 * a * c
    
    if d < 0:
        raise ValueError

    def solution(b, sqrt, a):
        return (-b + sqrt) / (2*a)
    return solution(b, sq(d), a), solution(b, -sq(d), a)

def main():
    while ((a := input("Inserisci il valore di A (ENTER per uscire): ")) != ""):
        b = int(input("Inserisci il valore di B: "))
        c = int(input("Inserisci il valore di C: "))
        try:
            print(solve_quadratic(int(a), b, c))
        except ValueError: 
            print("Errore! Delta minore di 0")
            
if __name__ == "__main__":
    main()