from random import randrange

def randchar(mi:int , ma: int):
    return chr(randint(randrange(mi, ma)))

def main():
    mi = int(input("min? "))
    ma = int(input("max? "))
    print(randchar(mi, ma))

if __name__ == "__main__":
    main()
