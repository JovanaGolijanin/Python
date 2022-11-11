#08

def izmeni(list):
    uzmi = 1
    rezultat = []
    suma = list[0]
    rezultat.append(suma)

    brojProlazaka =0
    while (brojProlazaka < len(list)-1):
        suma = list[0]
        for i, element in enumerate(list):
            if i < uzmi and i != (len(list)-1):
                suma += list[i+1] 
        rezultat.append(suma)    
        brojProlazaka += 1
        uzmi += 1
    return rezultat


print(izmeni([1, 2, 4, 7, 9]))