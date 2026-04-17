def sommanumeri(n):
    somma = 0
    for i in range(1, n+1):
        somma = somma + i
    return somma

num = int(input("Inserisci un numero: "))
out = sommanumeri(num)
print("Somma dei numeri da 1 a {}: {}".format(num, out))