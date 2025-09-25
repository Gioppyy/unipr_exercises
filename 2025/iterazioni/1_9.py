from random import randint
from time import sleep

TOP = 20
RESET = "\033[0m"

def get_color(n):
    if n > 0:
        return "\033[32m+"
    elif n == 0:
        return "\033[33m"
    else:
        return "\033[31m"

p1 = 0
p2 = 0

while (p1 < TOP and p2 < TOP):
    n1 = randint(-1, 3)
    p1 += n1
    if p1 + n1 < 0: p1 = 0

    n2 = randint(-1, 3)
    p2 += n2
    if p2 + n1 < 0: p2 = 0


    print(f"p1: {p1} {get_color(n1)}{n1} {RESET}- p2: {p2} {get_color(n2)}{n2} {RESET}")
    sleep(0.3)

print(f"Ha vinto: {"l'arrampicatore 1" if p1 >= TOP else "l'arrampicatore 2"}")
