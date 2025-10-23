from math import sqrt

def add_square(data, n):
    value = n ** 2
    data.append(value)

def main():
    values = []
    for _ in range(5):
        v = int(input("v? "))
        add_square(values, v)

    print(values)

if __name__ == "__main__":
    main()
