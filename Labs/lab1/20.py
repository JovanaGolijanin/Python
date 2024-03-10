
def boje(boja):
    
    recnik = {"Red": int(boja[1]+boja[2], 16), "Green": int(boja[3]+boja[4], 16), "Blue": int(boja[5]+boja[6], 16)}
    return recnik

print(boje("#FA1AA0"))