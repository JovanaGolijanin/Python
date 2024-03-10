from itertools import *

def spojidict(lista1:list, lista2:list)->list:
    return(list(map(lambda x: {'prvi': x[0], 'drugi' :x[1]}, zip_longest(lista1, lista2, fillvalue = '-'))))

print(spojidict([1, 7, 2, 4], [2, 5, 2]))