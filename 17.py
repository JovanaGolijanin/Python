
def kreiraj(n:int)->list:
    rez = []    
    i=0
    zbir = 0
    while i<=n:
        zbir += i
        kvadrat = pow(zbir,2)
        rez.append((i,kvadrat))
        i+=1
    return rez

print(kreiraj(4))