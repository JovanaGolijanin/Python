def stepenuj(l):
    rez = []
    for t in l:
        s = t[0]
        for x in t[1:]:
            s = s ** x
        rez.append(s)
    return rez


print(stepenuj([(1, 4, 2), (2, 5, 1), (2, 2, 2, 2), (5, )]))