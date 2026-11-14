esami = [
    ("analisi", 27),("fisica", 18),
    ("informatica", 30), ("algebra", 24)
]

e_max = esami[0]
for e in esami:
    if e[1] > e_max[1]:
        e_max = e

print("Esame con voto massimo:", e_max[0])

somma = 0
for e in esami:
    somma += e[1]

media = somma/len(esami)
print("Voto medio:", media)