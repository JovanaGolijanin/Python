#06

def razlika(list1, list2):
    nijeUListi = 0
    rezultat = []
    for elementPrve in list1:
        nijeUListi = 0
        for elementDruge in list2:
            if elementPrve == elementDruge:
                nijeUListi = 1
        if nijeUListi == 0:
            rezultat.append(elementPrve)
    return rezultat


print(razlika([1, 4, 6, "2", "6"], [4, 5, "2"]))