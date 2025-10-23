from string import ascii_uppercase

def main():
    n = int(input("n? "))
    #for i in range(n):
    #    print(ascii_uppercase[:i+1])

    for i in range(1, n+1):
        for j in range(i):
            code = ord("A") + j
            letter = chr(code)
            print(letter, end="")
        print()

    print()

    for i in range(n, 0, -1):
        for j in range(i):
            code = ord("A") + j
            letter = chr(code)
            print(letter, end="")
        print()


if __name__ == "__main__":
    main()
