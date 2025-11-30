def f(x):
    return x**3 - x - 1

def bisezione_ricorsiva(a, b):
    c = (a + b) / 2
    fc = f(c)

    if abs(fc) < 0.001:
        return (c, fc)

    if f(a) * fc < 0:
        return bisezione_ricorsiva(a, c)
    else:
        return bisezione_ricorsiva(c, b)

def main():
    x, fx = bisezione_ricorsiva(1,2)
    print(f"{x = } & f(x)={fx:.6f}")

if __name__ == "__main__":
    main()
