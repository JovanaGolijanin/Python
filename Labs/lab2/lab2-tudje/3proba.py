from itertools import zip_longest

def spoji(list1,list2):
    return list(map(lambda x:(x[0],x[1],x[0]+x[1]) if x[0]<x[1] else (x[1],x[0],x[0]+x[1]),list(zip_longest(list1,list2,fillvalue=0)) ))

print(spoji([1, 7, 2, 4], [2, 5, 2]))