
from functools import reduce


def presek(l1, l2):
    return list(filter(lambda x: x in l2, l1))


def izracunaj(l1):
    return list(map(lambda x: (x**2) if type(x) in (int, float) else reduce(lambda a, b: a + b**2, x, 0), l1))


print(presek([5, 4, "1", "8", 3, 7], [1, 9, "1", 3]))  # => "1", 3

# => [4, 16, 14, 20, 4, 106]
print(izracunaj([2, 4, [1, 2, 3], [4, 2], 2, [9, 5]]))