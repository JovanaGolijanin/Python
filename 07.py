#07

def operacija(list):
    rezultat = []
    for i, element in enumerate(list):
        suma = 0
        for tapl in list[i]:
            suma += tapl
        rezultat.append(suma)
    return rezultat

print(operacija([(1, 4, 6), (2, 4), (4, 1)]))