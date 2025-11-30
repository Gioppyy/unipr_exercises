def digits(n: int) -> list:
    d = []
    while n > 10:
        d.append(n % 10)
        n //= 10
    d.append(n)

    return d

def main():
    n = int(input("n? "))
    d = digits(n)

    t = 0
    for i, v in enumerate(d):
        t += v * (10**i)

    if t == n:
        print("Corretto!")
    else:
        print("Non funziona!")

if __name__ == "__main__":
    main()
