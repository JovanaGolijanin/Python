from functools import reduce


def unija(l1, l2):
    return list(reduce(lambda a, b: a if b not in a and a.append(b) else a, l2, l1))

# 14b ima uradjeno vec isto je kao neki zadatak


# =[5, 4, "1", "8", 3, 7, 9, 1] X [5, 4, '1', '8', 3, 7, 1, 9]  prvo se doda 1 pa 9? ne znam kako su dobili onaj raspored
print(unija([5, 4, "1", "8", 3, 7], [1, 9, "1"]))