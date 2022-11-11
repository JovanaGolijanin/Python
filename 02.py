#02

def numlista(list):
    recnik = {}
    for element in list:
            if type(element).__name__ not in recnik:
                recnik[type(element).__name__] = [element]
            else:
                recnik[type(element).__name__].append(element)
    return recnik

print(numlista(["Prvi", "Drugi", 2, 4, [3, 5]])) 
