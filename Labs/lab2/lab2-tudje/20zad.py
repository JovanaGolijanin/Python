def boje(heksa: str):
    bojedict = {"Red": int(heksa[1:3], 16), "Green": int(
        heksa[3:5], 16), "Blue": int(heksa[5:7], 16)}
    return bojedict


print(boje("#FA1AA0"))