def kreiraj(n):
    rez = []
    zbir = 0
    for i in range(n+1):
        zbir += i
        rez.append((i, zbir ** 2))
    return rez


print(kreiraj(4))