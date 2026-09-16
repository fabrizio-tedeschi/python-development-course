#Definizione della funzione
def potenza(base, esponente):
    if base == 0:
        return 0

    out = 1
    for i in range(0, esponente):
        out *= base
    return out

#Istruzioni di test
print("2^3 =", potenza(2, 3))
print("3^2 =", potenza(3, 2))
print("0^75 =", potenza(0, 75))
print("75^0 =",potenza(75, 0))