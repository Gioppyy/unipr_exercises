with open("outputserie.txt", "w") as out:
    with open("serie1.txt") as f1:
        for l1 in f1:
            with open("serie2.txt") as f2:
                for l2 in f2:
                    if int(l1) <= int(l2):
                        print(l1, end="", file=out)
                    else: print(l2, end="", file=out)
