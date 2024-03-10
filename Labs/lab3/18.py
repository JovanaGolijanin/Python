import random

class Node:
    def __init__(self, val):
        self.children = []
        self.info = val
    def addChild(self, child):
        self.children.append(child)
        return self
    def __str__(self):
        return f" {self.info} "
    def __repr__(self) -> str:
        return f" {self.info} "

def MakeThree(root, depth):
    if depth == 0:
        return
    for index in range(0, random.randint(0, 3)):
        child = Node(random.randint(0, 100))
        root.addChild(child)
        MakeThree(child, depth - 1)

def zad18(s, daljina):
    if len(s.children) == 0:
        return [daljina, [s]]
    maxDaljina = (0, None)
    for child in s.children:
        rezultat = zad18(child, daljina + 1)
        if maxDaljina[0] < rezultat[0]:
            maxDaljina = rezultat
        if maxDaljina[0] == rezultat[0]:
            maxDaljina[1] += rezultat[1]
    return maxDaljina

root = Node(random.randint(0, 100))
MakeThree(root,3)
rez = zad18(root, 1)
print(rez[0], rez[1])