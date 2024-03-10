
def izdvoji(lista:list)->list:
    rez = []
    n=0
    for i,x in enumerate(lista):
        if len(lista[i]) > n :
            rez.append(lista[i][n])
            n+=1
        else:
            rez.append(0)
            n+=1
    return rez

print(izdvoji([[5, 4, 4], [1, 9, 1], [5, 6], [4, 6, 10, 12]]))