def digits(n: int) -> list:
    d = []
    while n > 10:
        d.append(n % 10)
        n //= 10
    d.append(n)

    return d

def check_digits(l: list) -> int:
    r = 0
    for i in range(len(l)):
        r += (l[i] * pow(10, i))
    return r

digit = digits(6543)