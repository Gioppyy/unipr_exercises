def len_common_prefix(st1: str, st2: str):
    l1 = len(st1)
    l2 = len(st2)
    tot = 0

    for i in range(min(l1, l2)):
        if st1[i] == st2[i]:
            tot += 1
    return tot

def main():
    s1 = input("stringa 1? ")
    s2 = input("stringa 2? ")
    tot = len_common_prefix(s1, s2)
    print(f"{tot = }")

if __name__ == "__main__":
    main()
