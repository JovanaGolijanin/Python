from ctypes import resize


def kreiraj(l):
    rez = []
    for i in range(len(l)-1):
        nl = []
        l1 = l[i]
        l2 = l[i+1]
        for x in l1:
            if x not in l2:
                nl.append(x)
        rez.append(nl)
    return rez


print(kreiraj([[1, 2, 3], [2, 4, 5], [4, 5, 6, 7], [1, 5]]))