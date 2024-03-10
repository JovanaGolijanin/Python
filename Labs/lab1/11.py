
def razlika(list):
    rez = []
    for i, el in enumerate(list):
            if i != (len(list)-1):
                rez.append(list[i]-list[i+1])
    return rez

print(razlika([8, 5, 3, 1, 1])) # [3, 2, 2, 0]