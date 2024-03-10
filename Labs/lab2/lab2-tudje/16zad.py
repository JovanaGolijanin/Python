# broji koliko razlicitih tipova ima u dict izlaz
def brojanje(d: dict):
    rez = []
    l = d.values()
    types = []
    for x in l:
        if type(x) not in types:
            i = 0
            for y in l:
                if type(x) == type(y):
                    i += 1
            types.append(type(x))
            rez.append((type(x).__name__, i))
    return rez


# => [('int', 3), ('list', 2), ('str', 1)]
print(brojanje({1: 4, 2: [2, 3], 3: [5, 6], 4: 'test', 5: 9, 6: 8}))