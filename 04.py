#04

def zbir(list):
    rezultat = []
    for i , element in enumerate(list):
        if i != (len(list)-1):
            dodaj = element + list[i+1]
            rezultat.append(dodaj)
    return rezultat

print(zbir([1, 2, 3, 4, 5]))