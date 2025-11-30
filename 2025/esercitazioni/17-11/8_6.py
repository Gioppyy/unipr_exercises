from math import inf

class Node:
    def depth(self) -> int:
        raise NotImplementedError("Abstract method")

    def largest(self) -> tuple[int, str]:
        raise NotImplementedError("Abstract method")

    def print(self, indent: int):
        raise NotImplementedError("Abstract method")

class Document(Node):
    def __init__(self, name: str, text: str):
        self._name = name
        self._text = text

    def depth(self) -> int:
        return len(self._text)

    def largest(self):
        return self.size(), self._name

    def print(self, indent: int):
        print(" " * indent + self._name)

class Folder(Node):
    def __init__(self, name: str, subnodes: list[Node]):
        self._name = name
        self._subnodes = subnodes

    def depth(self) -> int:
        total_size = 0
        for n in self._subnodes:
            total_size += n.size()
        return total_size

    def largest(self):
        result = (-inf, "")
        size, path = max((n.largest() for n in self._subnodes), default=result)
        return size, self._name + "/" + path

    def print(self, indent: int):
        print(" " * indent + self._name)
        for n in self._subnodes:
            n.print(indent + 4)

def main():
    prod = Document("prod.csv", "1,2,3,4")
    data = Folder("data", [prod])
    a1_0 = Document("a1.txt", "bla bla 0")
    work = Folder("Work", [a1_0, data])
    a1_1 = Document("a1.txt", "a different file")
    personal = Folder("Personal", [a1_1])
    desktop = Folder("Desktop", [work, personal])

    print(desktop.depth())
    print(desktop.largest())
    print()
    desktop.print(0)
if __name__ == "__main__":
    main()
