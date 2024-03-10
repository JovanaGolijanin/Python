# Verzija sa rekurzijom glave (head recursion)
def factorial(n):
    if n == 0:
        return 1
    else:
       return factorial(n - 1) * n

print(factorial(5))

# Verzija sa repnom rekurzijom (tail recursion, bez optimizacije)
def factorialRR(n, acc = 1):
    if n == 0:
        return acc
    else:
        return factorialRR(n - 1, acc * n)

print(factorialRR(5))

#vraca naziv f-je
print.__qualname__

stampaj = print
stampaj.__qualname__

stampaj("Poruka")

def kvadratPP(x: int):
    broj = "Broj: " + str(x)
    return (x ** 2, broj) 

print(kvadratPP.__annotations__)

#kvadratPP(kvadratPP(10))

def kombinacijaFunkcija(drugaFja, prvaFja, broj: int):
    prviRez = prvaFja(broj)
    drugiRez = drugaFja(prviRez[0])
    return (drugiRez[0], prviRez[1] + ", " + drugiRez[1])

print(kombinacijaFunkcija(kvadratPP, kvadratPP, 2))

def fibonacci(n):
    if (n <= 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

from timeit import default_timer as timer
from datetime import timedelta

def testFibonacci():
    start = timer()
    val = fibonacci(40)
    end = timer()
    return (val, str(timedelta(seconds = end - start)))

print(testFibonacci())

from itertools import tee
from functools import reduce

def pairwise(iter):
    a,b = tee(iter)
    next(b, None)
    return zip(a,b)

def zbir(lista)->list[int]:
    return [reduce(lambda x ,y: x + y, z, 0) for z in list(pairwise(lista))]

print(zbir([1, 2, 3, 4, 5]))

def suma(lista):
    return reduce(lambda x, y: x + y, [z for z in [reduce(lambda p, q: p + q, r, 0) for r in lista]], 0)

print(suma([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))