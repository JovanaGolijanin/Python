from itertools import starmap


def zbir(l):
    return list(filter(lambda y: type(y) in (int, float), map(lambda x: x[1] + l[x[0] + 1] if x[0]+1 < len(l) else (), list(enumerate(l)))))
    # return list(filter(lambda y: type(y) in (int, float), starmap(lambda x, i: x + l[i+1] if i+1 < len(l) else (), enumerate(l))))


def suma(l, i=0):
    if type(l[i]) in (int, float):
        return l[i] + (suma(l, i+1) if len(l) > i+1 else 0)
    elif type(l[i]) is list:
        return suma(l[i], 0) + (suma(l, i+1) if len(l) > i+1 else 0)


# print(zbir([1, 2, 3, 4, 5]))

# print(suma([1, 1, [1, [1, [1, [[1]]]]], 1, [1, 1, [1, 1]]]))

print(suma([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))