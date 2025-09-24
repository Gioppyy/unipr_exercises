try: 
    n = int(input("Inserire il valore di N: "))
    m = []
    for i in range(n):
        r = []
        for j in range(n):
            r.append("a") 
        m.append(r)

    print(m)
except Exception as e:
    print(f"Numero Inserito non valido! {e}")