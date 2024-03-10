from functools import reduce


def prosek(l1):
    return list(map(lambda x: reduce(lambda a, b: a+b, x)/len(x), l1))


def zamena(l1, broj):
    return list(map(lambda x, i: reduce(lambda a, b: a+b, l1[i+1:]) if x < broj else x, l1, range(len(l1))))


print(prosek([[1, 4, 6, 2], [4, 6, 2, 7], [3, 5], [5, 6, 2, 7]]))
print(zamena([1, 7, 5, 4, 9, 1, 2, 7], 5))  # = [35, 7, 5, 19, 9, 9, 7, 7]