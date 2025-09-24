def check() -> int:
    name = input("What is your name? ")
    if name.lower() != "lancelot":
        return 0
    quest = input("What is your quest? ")
    if quest.lower() != "holy grail":
        return 0
    color = input("What is your favorite color? ")
    if color.lower() != "blue":
        return 0

    return 1

def main():
    if check():
        print("Right. Off you go.")
    else:
        print("Down into the Gorge of Ethernal Peril!")

if __name__ == "__main__":
    main()
