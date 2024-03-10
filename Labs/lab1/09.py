#09

def prosek(list):
    rezultat = []
    for i, element in enumerate(list):
        suma = 0 
        for podlista in list[i]:
            suma += podlista
        rezultat.append(suma / len(list[i]))
    return rezultat

print(prosek([[1, 4, 6, 2], [4, 6, 2, 7], [3, 5], [5, 6, 2, 7]]))