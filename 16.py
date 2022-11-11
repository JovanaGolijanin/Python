
def brojanje(recnik:dict)->list[tuple]:
    
    pom = []
    pom2= ()
    rez = []
    
    for el in recnik.values():
        if type(el).__name__ not in recnik.values():
            pom.append(type(el).__name__)

    for element in pom:
        count = 0
        for el in pom:
            if element == el:
                count +=1
        pom2 = (element, count) 
        if (element, count) not in rez: 
            rez.append(pom2)     

    return rez

print(brojanje({1 : 4, 2 : [2, 3], 3 : [5, 6], 4 : 'test', 5 : 9, 6 : 8}))