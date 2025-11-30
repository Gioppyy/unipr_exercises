def select_chars(txt: str) -> str:
    s = ""
    for i, c in enumerate(txt):
        if i == 0:
            s += c
            continue
        if c < txt[i - 1] or c < txt[i + 1]:
            continue
        s += c
    return s


def main():
    print(select_chars(input("txt? ")))


if __name__ == "__main__":
    main()
