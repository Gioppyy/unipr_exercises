def perfect_square(n: int) -> int:
    if n < 0:
        return False
    i = 0
    while i * i <= n:
        if i * i == n:
            return True
        i += 1
    return False

def main():
    print(perfect_square(int(input("Inserisci un numero: "))))

main()
