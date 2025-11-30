def find_max(l):
    if len(l) == 1:
        return l[0]

    if not any(isinstance(el, list) for el in l):
        return max(l)
    else:
        st = []
        for e in l:
            if isinstance(e, list):
                st.append(find_max(e))
            else:
                st.append(e)
        return max(st)

def main():
    print(find_max(["Ann", ["Bart", ["Carol", "Cindy"], "Bob", "Art"], ["Bea"], "Bill"]))

if __name__ == "__main__":
    main()
