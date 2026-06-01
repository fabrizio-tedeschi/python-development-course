n = int(input("Quanti valori vuoi inserire nella lista? "))

l = []
for i in range(n):
    x = int(input("inserisci numero: "))
    l.append(x)

l.sort()
l.reverse()

no_doppi = []
for e in l:
    if no_doppi.count(e) == 0:
        no_doppi.append(e)


print("Lista ordinata iniziale:", l)
print("Lista ordinata e senza duplicati:", no_doppi)