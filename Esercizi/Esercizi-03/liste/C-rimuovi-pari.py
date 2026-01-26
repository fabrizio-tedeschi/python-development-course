# Inizializzazioni
n = 6
numeri = []
pari = []

# Input e aggiunta dei valori della lista
for i in range(n):
    x = int(input("Inserisci un numero: "))
    numeri.append(x)



# Scorrimento della lista
for num in numeri:
    
    # Controllo se l'elemento è pari
    if num % 2 == 0:
        pari.append(num)

# Stampa dei risultati
print("Lista numeri pari:", pari)
print("Lunghezza della lista:", len(pari))