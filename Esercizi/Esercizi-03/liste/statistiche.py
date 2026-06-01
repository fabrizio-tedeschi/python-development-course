n = int(input("Numero di valori da inserire: "))

l = []
for i in range(n):
    x = int(input("Inserisci valore: "))
    l.append(x)
print(l)

somma = 0
prodotto = 1
conta = 0
for num in l:
    somma += num
    prodotto *= num
    conta += 1

print("Somma:", somma)
print("Prodotto:", prodotto)
print("Media:", somma/conta)

"""
In alternativa al ciclo for:
somma = sum(l)
media = sum(l) / len(l)
"""