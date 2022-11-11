#10

def izbroj(lista):
    suma = 0
    if isinstance(lista, list):
        for element in lista:
            suma += izbroj(element)
        return suma
    else:
        return 1

print(izbroj([1, [1, 3, [2, 4, 5, [5, 5], 4]], [2, 4], 4, 6]))