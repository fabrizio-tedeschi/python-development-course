# Input dei valori e inserimento nella lista
n = int(input("Quanti valori vuoi inserire nella lista? "))

l = []
for i in range(n):
    x = int(input("inserisci numero: "))
    l.append(x)

# Ordinamento della lista
l.sort()

# Per ogni elemento della lista
for e in l:
    # Fino a quando ci sono duplicati
    while l.count(e) > 1:
        l.remove(e)

print("Lista ordinata e senza duplicati:", l)