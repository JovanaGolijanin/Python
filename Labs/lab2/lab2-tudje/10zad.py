from functools import reduce


def izbroj(l1):
    return reduce(lambda a, b: a + (1 if type(b) in (int, float) else izbroj(b)), l1, 0)


def stepen(l1):
    return list(map(lambda x, i: x ** l1[i+1], l1[:-1], range(len(l1)-1)))


print(izbroj([1, [1, 3, [2, 4, 5, [5, 5], 4]], [2, 4], 4, 6]))  # = 13
print(stepen([1, 5, 2, 6, 1, 6, 3, 2, 9]))  # =[1, 25, 64, 6, 1, 216, 9, 512]