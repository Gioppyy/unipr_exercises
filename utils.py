# Ciclo senza index
for _ in range(1):
    pass

# Draw a cross
"""
    g2d.set_color((10, 10, 10))                 # Setto il colore casuale
    g2d.draw_line((x+4, y), (x-3, y), 2)        # Disegno la linea orizzontale
    g2d.draw_line((x, y+4), (x, y-3), 2)        # Disegno la linea verticale
"""

# Random color
import random
r, g, b = [random.randint(0,255) for _ in range(3)]

# Manage a file
"""
    with open("test.txt", "+r") as f:
        f.read() # read all the file's content
    f.close()

    with open("text.txt", "+a") as f:
        f.write("Ciao !")
    f.close()
"""

# Lambda expression
somma = lambda a, b : a+b
print(somma(1, 2)) # it will return 3

rn = lambda mi, ma : random.randint(mi, ma)
print(rn(1, 2)) # random number in 1, 2 range

# Tuple assignment 
def coord(a, b):
    return tuple((a,b))
def coord2(a, b):
    return (a, b)

c1 = coord(1,2) # -> (1, 2)
c2_1, c2_2 = coord2(1,2) # -> c2_1=1 | c2_2=2

# Manage an error
def divisione(a, b):
    if b == 0: raise ValueError("Denominatore minore di 0")
    return a // b

try:
    divisione(1,0)
except ValueError as e:
    print(e)

# Oneline condition
x = 1
print("uno" if x == 1 else "Non uno")

# One line list
my_list = [n for n in range(1, 11)]

# Get several input splitted by a char
my_input_list = [int(i) for i in input("Inserire una serie di numeri separati da virgole (Es. 1,2,3,4): ").split(",")]

# Pretty list print
print(*my_list) # -> 1 2 3 4 5 6 7 8 9 10

# Make a while cycle run until the input is empty (or any char)
while( (n := int(input("Inserisci un numero (0 for exit)"))) != 0):
    pass # Your code here... 