def recursive_pow(x: float, n: int) -> float:
    if n == 0:
        return 1
    elif n > 0:
        return x * recursive_pow(x, n - 1)

def main():
    x = float(input("x? "))
    n = int(input("n? "))

    print(f"{x} elevato alla potenza di {n} è: {recursive_pow(x, n)}")

if __name__ == "__main__":
    main()
