from itertools import *


def razlika(l1, l2):
    return list(filter(lambda x: x not in l2, l1))


def objedini(l1, l2):
    return list(starmap(lambda x, y: (x, y) if x < y else (y, x), zip_longest(l1, l2, fillvalue=0)))


print(razlika([1, 4, 6, "2", "6"], [4, 5, "2"]))
print(objedini([1, 7, 2, 4, 5], [2, 5, 2]))