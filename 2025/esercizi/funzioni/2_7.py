def common_divisors(a: int, b: int) -> list:
    divs = []
    for i in range(1, max(a, b)+1):
        if a % i == 0 and b % i == 0:
            divs.append(i)
    return divs

def main():
    a = int(input("Inserisci il numero a: "))
    b = int(input("Inserisci il numero b: "))
    print(common_divisors(a, b))

main()
