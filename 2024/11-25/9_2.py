from random import randrange

n = int(input("Inserisci quanti tiri fare: "))
for _ in range(n):
  print(f"{randrange(1,6)}  {randrange(1,6)}")

#whi#le((n := int(input("Inserisci quanti tiri fare (0 FOR EXIT):")) != 0)): 
#   # for _ in range(n):
#   #     print(f"{randrange(1,6)} {randrange(1,6)}") 
