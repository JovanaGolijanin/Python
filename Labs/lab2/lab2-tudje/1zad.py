from itertools import *


def parni(list):
    i = 0
    for x in list:
        if x % 2 == 0:
            i += 1
    return i


def parni2(l1):
    return len(list(filter(lambda x: x % 2 == 0, l1)))


def poredak(l1, l2):
    return list(starmap(lambda x, y: (x, y, "Jeste" if y > x else "Nije"), zip_longest(l1, l2, fillvalue=0)))


print(parni2([1, 4, 5, 2, 8, 2]))
print(poredak([1, 7, 2, 4], [2, 5, 2]))