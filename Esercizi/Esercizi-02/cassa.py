prezzo = float(input("Inserisci prezzo: "))

somma = 0
while prezzo != 0:
    somma += prezzo
    prezzo = float(input("Inserisci prezzo: "))

print("Totale:", somma)

pagato = float(input("Inserire contanti per pagare: "))
while pagato < somma:
    print("Valore inserito inferiore al totale")
    pagato = float(input("Inserire contanti per pagare: "))

resto = pagato - somma
print("Resto:", resto)