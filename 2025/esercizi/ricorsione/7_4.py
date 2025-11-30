from math import gcd

def mcd(a: int, b: int):
    if b == 0:
        return a
    else:
        return mcd(b, a%b)

def main():
    a = int(input("a? "))
    b = int(input("b? "))
    print("Ricorsivo: ", mcd(a, b))
    print("Python: ", gcd(a, b))

if __name__ == "__main__":
    main()
