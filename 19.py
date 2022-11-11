
def stepenuj(lista:list)->list:
    rez = []
    for i, el in enumerate(lista):
        pom = el[0]
        for k, smth in enumerate(el):
             if k < (len(el)-1):
                pom2 = pow(pom, el[k+1])
                pom = pom2
        rez.append(pom)

    return rez

print(stepenuj([(1, 4, 2), (2, 5, 1), (2, 2, 2, 2), (5, )])) 