from functools import *


def brojel(l1):
    return list(map(lambda x: len(x) if type(x) is list else -1, l1))

# ne znam da li mozemo da koristimo functools


def proizvod(l1, l2):
    return list(map(lambda x, y: reduce(lambda a, b: a + b, x) * y, l1, l2))


print(brojel([[1, 2, 3], 3, [1, 2]]))
print(proizvod([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3]))