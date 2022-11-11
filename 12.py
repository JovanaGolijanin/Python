
def presek(list1, list2):
    # return [x for x in list1 if x in list2]
    rez = []
    for i, el in enumerate(list1):
        if el in list2:
            rez.append(list1[i])
    return rez

print(presek([5, 4, "1", "8", 3, 7, 1], [1, 9, "1"]))