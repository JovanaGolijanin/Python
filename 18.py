
def kreiraj(lista:list)->list:
    rez = []
    for i, el in enumerate(lista):
            pom = []
            for j, smth in enumerate(el):
                if i < len(el)+1 and i < len(lista)+1:
                    if lista[i][j] not in lista[i+1]:
                        pom.append(lista[i][j])
            if pom != []:            
                rez.append(pom)
            
    return rez

print(kreiraj([[1, 2, 3], [2, 4, 5], [4, 5, 6, 7], [1, 5]])) 