def inp(i) -> int:
    try:
        r = int(input(f"Inserisci il valore della resistenza n.{i+1} [0 for EXIT]: "))
        return r
    except:
        return -99999999

def main():

    r = []
    i = 0
    while (n := inp(i)) != -99999999 and n != 0:
        r.append(n)
        i += 1

    #t = sum(r)
    t = 0
    for i in range(len(r)):
        t += r[i]
    print(f"Resistenza equivalente in serie: {t}")

    t = 0
    for i in range(len(r)):
        t += 1/r[i]
    print(f"Resistenza equivalente in parallelo: {t:.2f}")


if __name__ == "__main__":
    main()
