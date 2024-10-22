# Ciclo senza index
for _ in range(1):
    pass

# Random color
import random
r, g, b = [random.randint(0,255) for _ in range(3)]

# Manage a file
with open("test.txt", "+r") as f:
    f.read() # read all the file's content
f.close()

with open("text.txt", "+a") as f:
    f.write("Ciao !")
f.close()

# Lambda expression
sum = lambda a, b : a+b
sum(1, 2) # it will return 3
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