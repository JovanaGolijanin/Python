
from functools import reduce


def razlika(l1):
    return list(map(lambda x, i: x - l1[i+1], l1[:-1], range(len(l1)-1)))


def proizvod(l1):
    return reduce(lambda a, b: a*(b if type(b) in (int, float) else proizvod(b)), l1, 1)


print(razlika([8, 5, 3, 1, 1]))  # = [3, 2, 2, 0]
print(proizvod([[1, 3, 5], [2, [2, [2, 2]], 6], [1, 2, 3]]))  # = 8640