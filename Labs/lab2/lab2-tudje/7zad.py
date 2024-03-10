from functools import reduce


def operacija(l1, func):
    return list(map(lambda t: reduce(func, t), l1))


def dodajnaprvo(a: dict, b: dict):
    a.update(b)
    return a


def objedini(l1):
    return reduce(lambda a, b: dodajnaprvo(a, b), list(map(lambda x: {x: None} if type(x) in (int, float) else {x[0]: list(map(lambda z: z[1], filter(lambda y: y[0] > 0, enumerate(list(x)))))}, l1)))


def objedini2(l1):
    listaDict = list(map(lambda a: {a[0]: list(a[1:])} if (
        type(a) is tuple) else {a: None}, l1))
    return {list(x.keys())[0]: x.get(list(x.keys())[0]) for x in listaDict}


print(operacija([(1, 4, 6), (2, 4), (4, 1)], lambda x, y: x + y))
print(objedini2([(1), (3, 4, 5), (7), (1, 4, 5), (6, 2, 1, 3)]))