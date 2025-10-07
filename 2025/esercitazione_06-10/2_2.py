def all_alpha(s: str) -> bool:
    for c in s:
        if c == ' ':
            continue
        if not (('a' <= c <= 'z') or ('A' <= c <= 'Z')):
            return False
    return True

def main():
    s = input("Inserisci una stringa: ")
    print(f"Solo caratteri? {all_alpha(s)}")

if __name__ == "__main__":
    main()
