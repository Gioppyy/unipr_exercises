def inp() -> int:
    try:
        n = int(input("Inserisci un numero intero [0 for EXIT]: "))
        return n
    except:
        return 0

def main():
    nums = []
    while (n := inp()) != 0:
        nums.append(n)

    media = sum(nums) / len(nums)
    sotto, sopra = [], []
    for n in nums:
        if n < media:
            sotto.append(n)
        else:
            sopra.append(n)

    print(f"Media: {media}")
    print(f"Numeri sotto: {sotto}")
    print(f"Numeri sopra: {sopra}")

if __name__ == "__main__":
    main()
