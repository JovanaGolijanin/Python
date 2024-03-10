def izdvoji(l1):
    return list(map(lambda x, i: 0 if len(x) <= i else x[i], l1, range(len(l1))))


def promeni(l1, broj):
    return list(map(lambda x: x + (-broj if x > broj else broj), l1))


# =[5, 9, 0, 12]
print(izdvoji([[5, 4, 4], [1, 9, 1], [5, 6], [4, 6, 10, 12]]))
print(promeni([7, 1, 3, 5, 6, 2], 3))  # = [4, 4, 6, 2, 3, 5]