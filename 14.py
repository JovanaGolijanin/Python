
def unija(list1:list[object], list2:list[object])->list[object]:
    rez = []
    for i,el in enumerate(list1):
        rez.append(el)
    for i, el in enumerate(list2):
        if el not in rez:
            rez.append(list2[i])       
    return rez

print(unija([5, 4, "1", "8", 7], [1, 9, "1"]))