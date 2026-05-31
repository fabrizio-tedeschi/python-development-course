n = -1
somma = 0
prodotto = 1

while n != 0:
    n = int(input("Inserire un valore (0 per terminare): "))
    somma += n

    if n != 0:
        prodotto *= n

print("Stampo la somma dei valori:", somma)
print("Stampo il prodotto dei valori:", prodotto)