def somma_numeri(n):
    somma = 0
    for i in range(1, n+1):
        somma = somma + i
    return somma

num = int(input("Inserisci un numero: "))
out = somma_numeri(num)
print("Somma dei numeri da 1 a {}: {}".format(num, out))