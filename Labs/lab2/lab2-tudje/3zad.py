from itertools import *

def spoji(list1,list2):
    return list(starmap(lambda x, y: (x, y, x + y), zip_longest(list1,list2, fillvalue=0)))

print(spoji([1, 7, 2, 4], [2, 5, 2]))