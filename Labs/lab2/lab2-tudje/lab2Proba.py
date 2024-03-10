print("----------------1-------------------")
#1
from itertools import zip_longest

def poredak(lista1,lista2):
    return list(map(lambda x: (x[0],x[1], ('Jeste') if x[0]!=0 and x[1]/x[0] == 2 else ('Nije')),zip_longest(lista1,lista2,fillvalue=0)))
print(poredak ([1, 7, 2, 4], [2, 5, 2]))

print("----------------2-------------------")
#2

def spojidict(lista1,lista2):
    return list(map(lambda x:{'prvi':x[0], 'drugi':x[1]},zip_longest(lista1,lista2,fillvalue='-')))

print(spojidict([1, 7, 2, 4], [2, 5, 2]))

print("----------------3-------------------")
#3

def spoji(lista1,lista2):
    return list(map(lambda x:(x[0],x[1],x[0]+x[1]) if x[0]<x[1] else (x[1],x[0],x[0]+x[1]),zip_longest(lista1,lista2,fillvalue=0) ))

print(spoji([1, 7, 2, 4], [2, 5, 2]))

print("----------------4-------------------")
#4
from functools import reduce

def suma(lista):
    return int(reduce(lambda x,y: x + y,[z for z in [reduce(lambda p,q: p + q, r) for r in lista]]))

print(suma([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))

print("----------------5-------------------")
#5

def proizvod(lista1,lista2):
    return list(map(lambda x:x[0]*x[1],zip([z for z in [reduce(lambda p,q: p+q,r) for r in lista1]],lista2)))

print(proizvod([[1,2,3],[4,5,6],[7,8,9]], [1,2,3]))

print("----------------6-------------------")
#6

def objedini(lista1,lista2):
    return list(map(lambda x:(x[0],x[1]) if x[0]<=x[1] else (x[1],x[0]),zip_longest(lista1,lista2,fillvalue=0)))

print(objedini([1, 7, 2, 4, 5], [2, 5, 2]))

print("----------------7-------------------")
#7

def objedini(lista):
   return { lista[i][0] : list(lista[i][1:]) if len(lista[i]) > 2 else None for i in range(len(lista))}  # meni ne radi
print(objedini([(1,), (3, 4, 5), (7,), (1, 4, 5), (6, 2, 1, 3)]))


print("----------------8-------------------")
#8

def izracunaj(lista):
    return list(map(lambda x:x if type(x)==int else reduce(lambda p,q:p*q,x),lista))

print(izracunaj([1, 5, [1, 5, 3], [4, 2], 2, [6, 3]]))

print("----------------9-------------------")
#9

def zamena(lista,n):
    return list(lista[i] if(lista[i]>=5) else (reduce(lambda x,y:x+y,lista[i+1:])) for i in range(0,len(lista)))

print (zamena([1, 7, 5, 4, 9, 1, 2, 7], 5))

print("----------------10-------------------")
#10
from itertools import pairwise

def stepen(lista):
    return list(map(lambda x:x[0]**x[1],pairwise(lista)))

print(stepen([1, 5, 2, 6, 1, 6, 3, 2, 9]))

print("----------------11-------------------")
#11

def proizvod(lista):
    return int(reduce(lambda x,y:x*y,[z for z in [reduce(lambda p,q:p*q,r) for r in lista]]))

print(proizvod([[1, 3, 5],[2, 4, 6],[1, 2, 3]]))

print("----------------12-------------------")
#12

def izracunaj(lista):
    return list(map(lambda x:(x**2) if type(x)==int else reduce(lambda p,q:p+q**2,x,0),lista))

print(izracunaj([2, 4, [1, 2, 3], [4, 2], 2, [9, 5]]))

print("----------------13-------------------")
#13

def skupi(lista):
    return list(map(lambda x:list(map(lambda y:y[0]+y[1],zip_longest(x[0],x[1],fillvalue=0))),pairwise(lista)))      # ([1, 3, 5],[2, 4, 6])  ///  ([2, 4, 6],[1, 2])

print(skupi([[1, 3, 5],[2, 4, 6],[1, 2]]))


print("----------------14-------------------")
#14

def suma(lista):
    return list(map(lambda x:reduce(lambda p,q:p+q,x,0),lista))

print(suma([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))

print("----------------15-------------------")
#15

def promeni(lista,n):
    return list(map(lambda x:x+n if x<n else x-n,lista))

print(promeni([7, 1, 3, 5, 6, 2], 3))

print("----------------16-------------------")
#16

def broj(br):
    return (int(br[1:],base=16))

print(broj("#FA0EA0"))

print("----------------17-------------------")
#17

import re

def tekst(txt):
    return list(x if (ord(x)>=65 and ord(x)<=90) or (ord(x)>=97 and ord(x)<=122) or (ord(x)>=48 and ord(x)<=57) else '\\' + '\\u' + re.sub('0x', '', hex(ord(x))).zfill(4) for x in txt  )

print( ''.join(tekst("Otpornost 10Ω.")))

print("----------------18-------------------")
#18
import re

def brojevi(niz):
    return list(int(x) for x in re.findall(r'(\d+)',niz))

print(brojevi("42+10=52;10*10=100"))

print("----------------19-------------------")
#19
from itertools import groupby

def brojanje(niz):
    return max(len(list(i)) for j,i in groupby(niz))

print(brojanje("aatesttovi"))

print("----------------20-------------------")
#20

def izracunaj(lista, funkcija):
    return list(funkcija(lista[i], lista[i+1], lista[i+2]) for i in range(0, len(lista)-2))

print( izracunaj([2, 5, 1, 6, 7], lambda x, y, z: x + y * z) )
