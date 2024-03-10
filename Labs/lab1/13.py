
def izmeni(list):
    pp = []
    np = []
    rez = {}
    for i, el in enumerate(list):
        if i%2 == 0:
            pp.append(list[i]+1)
        else:
            np.append(list[i]-1)
    
    rez = {"pp": pp, "np" :np}
    return rez

print(izmeni([8, 6, 3, 1, 1]))