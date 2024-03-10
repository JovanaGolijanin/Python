import string
import sys

matrica = []
igraPrvi = 0
naPotezu = 'X'
brojVrsta = 0
brojKolona = 0

#Implementirati funkcije koje obezbeđuju unos početnih parametara igre
def init():
    global matrica
    global brojVrsta
    global brojKolona

    print("Unesite broj vrsta:")
    brojVrsta = int(sys.stdin.readline())

    print("Unesite broj kolona:")
    brojKolona = int(sys.stdin.readline())

    matrica = [ [ " " for i in range(brojKolona) ] for j in range(brojVrsta) ]

#Implementirati funkcije koje obezbeđuju prikaz proizvoljnog stanja problema (igre)
def stampaj(matrica):
    top(brojKolona)

    for x in range(0,brojVrsta):
        print(str(brojVrsta-x)+"||",end='')
        for num in range(0,brojKolona):
            print(matrica[x][num]+'|',end='')
        print("|"+str(brojVrsta-x))
        
    bottom(brojKolona)    

def top(brojKolona):
    print('  ',end='')
    for num in range(0,brojKolona):
        print(' '+string.ascii_uppercase[num],end='')
    print('')
    print('  ',end='')
    for num in range(0,brojKolona):
        print(' =',end='')
    print('')

def bottom(brojKolona):
    print('  ',end='')
    for num in range(0,brojKolona):
        print(' =',end='')
    print('')
    print('  ',end='')
    for num in range(0,brojKolona):
        print(' '+string.ascii_uppercase[num],end='')
    print('')


#Realizovati funkcije koje proveravaju da li je potez valjan
# vrsta 1..N | kolona A..Z
def potezValjan(vrsta,kolona): 
    kol = ord(kolona)-65
    vrs = brojVrsta-vrsta

    if(vrs<0 or kol<0):
        return False
    
    if(naPotezu=='X'):

        if((vrs+1)>=brojVrsta or kol>=brojKolona):
            return False

        if(matrica[vrs][kol]==' ' and matrica[vrs+1][kol]==' '):
            return True
        else:
            return False
    else:
        if(vrs>=brojVrsta or (kol+1)>=brojKolona):
            return False

        if(matrica[vrs][kol]==' ' and matrica[vrs][kol+1]==' '):
            return True
        else:
            return False

#Realizovati funkcije koje na osnovu zadatog poteza igrača menjaju trenutno stanjeproblema (igre) i prelaze u novo
def odigrajPotez(vrsta,kolona):
    global matrica
    global naPotezu

    if(potezValjan(vrsta,kolona)):
        kol = ord(kolona)-65
        vrs = brojVrsta-vrsta
        if(naPotezu=='X'):
            matrica[vrs][kol]='X'
            matrica[vrs+1][kol]='X'
            naPotezu='O'
        else:
            matrica[vrs][kol]='O'
            matrica[vrs][kol+1]='O'
            naPotezu='X'
        krajIgre()
        stampaj(matrica)
    else:
        print("Uneli ste nevalidni potez!")
    return matrica

#Napisati funkcije za proveru kraja igre
def krajIgre():
    if(naPotezu=='X'):
        for i in range(0,brojVrsta-1):
            for j in range(0,brojKolona):
                if(matrica[i][j]==' ' and matrica[i+1][j]==' '):
                    return False
    else:
        for i in range(0,brojVrsta):
            for j in range(0,brojKolona-1):
                if(matrica[i][j]==' ' and matrica[i][j+1]==' '):
                    return False
    return True #Kraj je igre zato sto nema slobodnih polja za igraca koj je na potezu


#Omogućiti izbor ko će igrati prvi (čovek ili računar)
def koIgraPrvi():
    global igraPrvi

    print("Ko igra prvi? (0-covek, 1-racunar):")
    igraPrvi = int(sys.stdin.readline())
    if(igraPrvi==0):
        print("Covek je prvi na potezu!")
    else:
        print("Racunar je prvi na potezu!")

#Realizovati funkcije koje na osnovu zadatog igrača na potezu i zadatog stanje igre formiraju sva moguća stanja igre (sve moguće table)
def svaMogucaStanja():
    if(naPotezu=='X'):
        for i in range(0,brojVrsta-1):
            for j in range(0,brojKolona):
                if(matrica[i][j]==' ' and matrica[i+1][j]==' '):
                    matrica[i][j] = 'X'
                    matrica[i+1][j] = 'X'
                    stampaj(matrica)
                    matrica[i][j] = ' '
                    matrica[i+1][j] = ' '

    else:
        for i in range(0,brojVrsta):
            for j in range(0,brojKolona-1):
                if(matrica[i][j]==' ' and matrica[i][j+1]==' '):
                    matrica[i][j] = 'O'
                    matrica[i][j+1] = 'O'
                    stampaj(matrica)
                    matrica[i][j] = ' '
                    matrica[i][j+1] = ' '

# Implementirati funkciju koja vrši procenu stanja
# Kao parametre treba da ima igrača za kojeg računa valjanost stanja, kao i samo stanje za koje se računa procena.
def heuristika(matrica, igrac):
    # Prebroji broj X i O na tabli
    x_broj = 0
    o_broj = 0

    for vrsta in matrica:
        for polje in vrsta:
            if polje == "X":
                x_broj += 1
            elif polje == "O":
                    o_broj += 1

    # Ako X ima vise, vrati pozitivnu vrednost
    if x_broj > o_broj:
        return x_broj - o_broj
    # Ako O ima vise, vrati negativnu vrednost
    elif o_broj > x_broj:
        return x_broj - o_broj
    # Ako oba igrača imaju isti broj odigranih, vrati 0
    else:
        return 0

# Vraća listu validnih poteza za trenutnog igrača.
def validni_potezi(matrica):
    # Ako je na redu "X", proverite da li ima praznih parova susednih ćelija u istoj koloni
    if naPotezu == "X":
        return [(i, j) for i in range(brojVrsta - 1) for j in range(brojKolona) if matrica[i][j] == " " and matrica[i + 1][j] == " "]
    # Ako je na redu "O", proverite da li ima praznih parova susednih ćelija u istom redu
    else:
        return [(i, j) for i in range(brojVrsta) for j in range(brojKolona - 1) if matrica[i][j] == " " and matrica[i][j + 1] == " "]

# Funkcija minimaks uzima trenutno stanje, trenutnu dubinu stabla pretrage i alfa i beta vrednosti za alfa-beta odescanje. 
# Vraća najbolju vrednost i najbolji potez za trenutnog igrača.

# Implementirati Min-Max algoritam sa alfa-beta odsecanjem na osnovu:
# zadatog stanja problema, dubine pretraživanja, procene stanja (heuristike) koja se određuje kada se dostigne zadata dubina traženja
# Treba vratiti potez koji treba odigrati ili stanje u koje treba preći
def minimax(matrica, dubina: int, alpha: int, beta: int):
    # Ako je igra završena ili smo dostigli maksimalnu dubinu pretrage, vracamo heuristiku trenutnog stanja
    kraj= krajIgre()
    if kraj == True or dubina == 0:
        return heuristika(matrica), None
    
    #Inicijalizuje najbolji_potez na None i najbolju_vrednost na veliki negativan broj za igrača koji maksimizira ili veliki pozitivan broj za igrača koji minimizira
    najbolji_potez = None
    if naPotezu == "X":
        #najbolja_vrednost = float("-inf") 
        najbolja_vrednost = -2000
        for potez in validni_potezi(matrica):
            # Napravi potez i rekurzivno poziva minimaks za rezultujuće stanje
            sledece_stanje = odigrajPotez(potez[0], potez[1])
            vrednost, _ = minimax(sledece_stanje, dubina - 1, alpha, beta)
            # Ažurira najbolju vrednost i najbolji potez ako je potrebno
            if vrednost > najbolja_vrednost:
                najbolja_vrednost = vrednost
                najbolji_potez = potez
            # Ažurira alfa za alfa-beta odescanje
            alpha = max(alpha, najbolja_vrednost)
            # Ako je beta manje ili jednako alfa, ne vrsimo dalju pretragu
            if beta <= alpha:
                break
    else:
        #najbolja_vrednost = float("inf")
        najbolja_vrednost = 2000
        for potez in validni_potezi(matrica):
            # Napravi potez i rekurzivno poziva minimaks za rezultujuće stanje
            sledece_stanje = odigrajPotez(potez[0], potez[1])
            vrednost, _ = minimax(sledece_stanje, dubina - 1, alpha, beta)
            # Ažurira najbolju vrednost i najbolji potez ako je potrebno
            if vrednost < najbolja_vrednost:
                najbolja_vrednost = vrednost
                najbolji_potez = potez
            # Ažurira beta za alfa-beta odescanje
            beta = min(beta, najbolja_vrednost)
            # Ako je beta manje ili jednako alfa, ne vrsimo dalju pretragu
            if beta <= alpha:
                break
    # Vracamo najbolju vrednost i odgovarajući najbolji potez
    return najbolja_vrednost, najbolji_potez

def start():
    global kraj
    global matrica

    koIgraPrvi()
    init()
    stampaj(matrica)

    dubina = 3

    while True:
        if(krajIgre()):
            pobedio=""
            if(naPotezu=='X'):
                pobedio='O'
            else:
                pobedio='X'
            print("Kraj Igre, pobedio je igrac "+pobedio+"!!!")
            break

# Ako je na redu računar, koristimo minimaks algoritam da odredimo najbolji potez
        if naPotezu == "O":
            vrednost, potez = minimax(matrica, dubina, -2000, 2000)
            print("Igrac " + naPotezu + " je odabrao potez:", potez)
            odigrajPotez(potez[0], potez[1])

        print("\nIgrac "+naPotezu+" na potezu")
        print("Unesite vrstu (broj 1..N)(-1 prekid igre, -2 stampanje svih mogucih stanja):")
        vrsta = int(sys.stdin.readline())
        if vrsta == -1:
            break
        else:
            if vrsta == -2:
                svaMogucaStanja()
                print("Unesite vrstu (broj 1..N)(-1 prekid igre, -2 stampanje svih mogucih stanja):")
                vrsta = int(sys.stdin.readline())
                print("Unesite kolonu (slovo A..Z):")
                kolona = sys.stdin.readline()
                odigrajPotez(vrsta,kolona[0])
            else:
                print("Unesite kolonu (slovo A..Z):")
                kolona = sys.stdin.readline()
                odigrajPotez(vrsta,kolona[0])
            
start()