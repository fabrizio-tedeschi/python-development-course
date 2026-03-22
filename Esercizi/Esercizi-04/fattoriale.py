#Definizione della funzione
def fattoriale(n):
    out = 1
    for i in range(1, n+1):
        out *= i
    return out

#Istruzioni di test
print("0! =", fattoriale(0))
print("1! =", fattoriale(1))
print("2! =", fattoriale(2))
print("5! =", fattoriale(5))