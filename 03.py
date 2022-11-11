#03

def uredi(list,N, vrednost):
    for i, element in enumerate(list):
        if i<N:
            list[i] += vrednost
        else:
            list[i] -= vrednost
    return list


print(uredi([1, 2, 3, 4, 5], 3, 1))