from functools import reduce

def suma(lista:list)->int:
    return int(reduce(lambda a, b: a + b,[zbir for zbir in [reduce(lambda s, x: s + x, podlista) for podlista in lista]]))

#     ((s+x) for x in pom)

   
#  def suma(lista):
#     return int(reduce(lambda x,y: x + y,[z for z in [reduce(lambda p,q: p + q, r) for r in lista]]))


print(suma([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))