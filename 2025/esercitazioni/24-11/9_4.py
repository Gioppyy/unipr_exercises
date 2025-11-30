from collections import defaultdict
import re

def main():
    with open("g2d.py", "r") as f:
        lines = f.readlines()
        tot = []
        for line in lines:
            tot += re.split(r"\W+", line)

        word_counts = defaultdict(int)
        for word in tot:
            if word:
                word_counts[word] += 1

    for word, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"'{word}': {count}")

if __name__ == "__main__":
    main()
