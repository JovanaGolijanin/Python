from itertools import *

def poredak(lista1:list, lista2:list)->list:
    return list(map(lambda x: (x[0], x[1], "Jeste ") if x[0]*2 == x[1]  else (x[0], x[1], "Nije"),zip_longest(lista1, lista2, fillvalue = 0)))
    
print(poredak ([1, 7, 2, 4], [2, 5, 2]))
