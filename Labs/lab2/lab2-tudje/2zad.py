from itertools import starmap, zip_longest


def numlista(lista):
    return list(filter(lambda x: type(x) in (int, float), lista))


def spojidict(l1, l2):
    return list(starmap(lambda x, y: {"prvi": x, "drugi": y}, zip_longest(l1, l2, fillvalue='-')))


print(numlista(["Prvi", "Drugi", 2, 4, [3, 5]]))
print(spojidict([1, 7, 2, 4], [2, 5, 2]))