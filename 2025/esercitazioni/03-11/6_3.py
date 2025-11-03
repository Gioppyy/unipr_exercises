from random import randint

def main():
    ris = [0] * 13
    n = int(input("n? "))

    for i in range(n):
        r = randint(2, 12)
        print(f"lancio n.{i+1}: e' uscito {r}")
        ris[r] += 1

    for i, t in enumerate(ris):
        print(f"{i}: {t}")

if __name__ == "__main__":
    main()
