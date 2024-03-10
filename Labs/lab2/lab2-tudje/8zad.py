from functools import reduce


def izmeni(l1):
    l2 = l1.copy()
    for x in range(len(l2)):
        if (x == 0):
            continue
        else:
            l2[x] = l2[x-1] + l2[x]
    return l2


def izracunaj(l1):
    return list(map(lambda x: reduce(lambda a, b: a*b, x) if type(x) is list else x, l1))


print(izmeni([1, 2, 3, 4, 5]))
print(izracunaj([1, 5, [1, 5, 3], [4, 2], 2, [6, 3]]))