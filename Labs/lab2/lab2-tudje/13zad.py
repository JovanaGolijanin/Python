def izmeni(l1):
    return list(map(lambda x, i: x + (-1 if i % 2 == 1 else 1), l1, range(len(l1))))


def dodaj(l1, l2):
    kraca = l1 if len(l1) < len(l2) else l2
    duza = l1 if len(l1) >= len(l2) else l2
    nule = [0] * (len(duza) - len(kraca))
    kraca.extend(nule)
    return list(map(lambda a, b: a+b, l1, l2))


def skupi(l1):
    return list(map(lambda x, i: dodaj(x, l1[i+1]), l1[:-1], range(len(l1)-1)))


# lambda a,b : a+b, x if len(x) >= len(l1[i+1]) else list(x).extend([0]* (len(l1[i+1] - len(x)))), l1[i+1] if len(l1[i+1]) >= len(x) else list(l1[i+1]).extend([0]*(len(x) - len(l1[i+1])))
# ne moze ovako jer extend ne vraca referencu na listu........ zasto ????!?!?!?! Nervira me sto to ne radi automatski mnogo bi lakse bilo... ili da lambda funckije mogu da budu kao u js vise reda
# =>[9, 4, 4, 0, 0] XXXXXX treba [9, 4, 4, 0, 2] = [8+1, 5-1, 3+1, 1-1, 1+1] ?? greska?
print(izmeni([8, 5, 3, 1, 1]))
print(skupi([[1, 3, 5], [2, 4, 6], [1, 2]]))  # = [[3, 7, 11], [3, 6, 6]]