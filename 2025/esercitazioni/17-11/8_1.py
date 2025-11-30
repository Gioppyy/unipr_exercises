def digits(n: int) -> list:
    d = []
    while n > 10:
        d.append(n % 10)
        n //= 10
    d.append(n)

    return d

def sum_digits(n: int):
    return n if n < 10 else sum_digits(sum(digits(n)))

def main():
    while n := int(input("n? ")):
        print(sum_digits(n))

if __name__ == "__main__":
    main()
