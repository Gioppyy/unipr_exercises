def digits(n: int) -> list:
    d = []
    while n > 10:
        d.append(n % 10)
        n //= 10
    d.append(n)

    return d

print(digits(6543))
