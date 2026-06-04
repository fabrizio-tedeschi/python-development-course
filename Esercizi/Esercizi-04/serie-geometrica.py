def serie_geometrica(n, q):
    s = 0
    for i in range(n+1):
        s = s + q**i
    return s

n = int(input("Inserire valore n: "))
while n <= 0:
    print("ERRORE: n deve essere positivo!")
    n = int(input("Inserire valore n: "))

q = int(input("Inserire valore q: "))
while q <= 0:
    print("ERRORE: q deve essere positivo!")
    q = int(input("Inserire valore q: "))

out = serie_geometrica(n, q)
print("Risultato:", out)