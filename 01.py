#01

def parni(list):
    parni = []
    neparni = []
    for element in list:
        if element%2 == 0:
            parni.append(element)
        else:
            neparni.append(element)
    recnik= {
                "Parni" : parni,
                "Neparni" : neparni
            }
    return recnik
    
print(parni([1, 7, 2, 4, 5]))