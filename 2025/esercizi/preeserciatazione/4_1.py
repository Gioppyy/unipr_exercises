from math import sqrt

def f(x):
    return x ** 3 + x**2 + sqrt(x) - 100

def approx_zero(a, b):
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("Non passa per zero scemotto")
    c = (a+b) / 2
    fc = f(c)

    if fa * fc < 0:
        return (a, c)
    else:
        return (c, b)

def main():
    a = float(input("a? "))
    b = float(input("b? "))

    for _ in range(10):
        a, b = approx_zero(a, b)
        print(f"{a = }, {b = }")

if __name__ == "__main__":
    main()
