#05

def brojel(list):
    rezultat = []
    for i, element in enumerate(list):
        count = 0
        if type(element).__name__ == 'list':
            for elementPodliste in list[i]:
                count +=1
            rezultat.append(count)
        else:
            rezultat.append(-1)
    return rezultat


print(brojel([[1, 2], [3, 4, 5], 'el', ['1', 1]]))
