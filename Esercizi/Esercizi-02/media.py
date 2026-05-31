n = -1
somma = 0
count = 0

while True:
    n = int(input("Inserire un voto: "))
    if n == 0:
        break
    somma += n
    count += 1

#Stampa dei risultati
print("La media dei tuoi voti: ", somma/count)