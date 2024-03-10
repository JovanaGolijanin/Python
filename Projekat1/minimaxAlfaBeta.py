class Symbol(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name
(A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z) = (Symbol(x) for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z) = (A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z)


lsv = [(A, 1), (C, 10), (M, 5)]

#heuristika
def proceni_stanje(stanje):
    procena = {
        K: 2, L: 3, M: 5, N: 9, O: 0, P: 7,
        Q: 4, R: 2, S: 1, T: 5, U: 6
    }
    return procena[stanje] if stanje in procena else 0

#u koja se sve stanja prelazi
def nova_stanja(stanje):
    stablo = {
        A: [B, C, D], B: [E, F], C: [G, H], D: [I, J],
        E: [K, L], F: [M, N], G: [O], H: [P, Q],
        I: [R, S], J: [T, U]
    }
    return stablo[stanje] if stanje in stablo else None

#najveca vrednost heuristike
def max_stanje(lsv):
    return max(lsv, key=lambda x: x[1])

#najmanja vrednost heuristike
def min_stanje(lsv):
    return min(lsv, key=lambda x: x[1])

# def minimax(stanje, dubina, moj_potez):
#     lista_poteza = nova_stanja(stanje)
#     min_max_stanje = max_stanje if moj_potez else min_stanje
#     if dubina == 0 or lista_poteza is None:
#         return(stanje, proceni_stanje(stanje))
#     return min_max_stanje([minimax(x, dubina - 1, not moj_potez) for x in lista_poteza])

#print(minimax(A, 2, 1))

def max_value(stanje, dubina, alpha, beta):
    lista_novih_stanja = nova_stanja(stanje)
    if dubina == 0 or lista_novih_stanja is None:
        return (stanje, proceni_stanje(stanje))
    else:
        for s in lista_novih_stanja:
            alpha = max(alpha,
                min_value(s, dubina - 1, alpha, beta),
                key = lambda x: x[1])
            if alpha[1] >= beta[1]:
                return beta
    return alpha

def min_value(stanje, dubina, alpha, beta):
    lista_novih_stanja = nova_stanja(stanje)
    if dubina == 0 or lista_novih_stanja is None:
        return (stanje, proceni_stanje(stanje))
    else:
        for s in lista_novih_stanja:
            beta = min(beta,
                max_value(s, dubina - 1, alpha, beta),
                key = lambda x: x[1])
        if beta[1] <= alpha[1]:
            return alpha
    return beta

def minimax(stanje, dubina, moj_potez, alpha = (A, 0), beta = (A, 10)):
    if moj_potez:
        return max_value(stanje, dubina, alpha, beta)
    else:
        return min_value(stanje, dubina, alpha, beta)

print(minimax(B, 2, 0))