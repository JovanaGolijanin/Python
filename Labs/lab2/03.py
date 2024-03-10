from itertools import zip_longest

def spoji(lista1, lista2):
    return list(map(lambda x: (x[0],x[1],x[0]+x[1]) if x[0]<x[1] else (x[1],x[0],x[0]+x[1]),zip_longest(lista1, lista2, fillvalue = 0)))

print(spoji([1, 7, 2, 4], [2, 5, 2]))