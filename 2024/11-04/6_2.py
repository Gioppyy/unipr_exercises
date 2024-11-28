
def strToUpper(s):
    ast = False
    nT = ""
    
    for c in s:
        if not ast and c == "*":
            ast = True
        elif ast:
            if c == "*":        
                ast = False
            else:
                nT += c.upper()
        else:
            nT += c

    return nT

text = input("Inserisci una stringa: ")
print(strToUpper(text))