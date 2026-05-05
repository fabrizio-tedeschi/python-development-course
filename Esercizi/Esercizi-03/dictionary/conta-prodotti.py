# Inizializzazione dictionary vuoto
carrello = {}

# Input del numero di prodotti da inserire
n = int(input("Inserisci numero di prodotti da acquistare: "))

# Inserimento di n prodotti
for i in range(n):
    
    prod = input("Inserisci un prodotto: ")
    
    # Se la chiave esiste allora incremento il valore
    if(carrello.get(prod) != None):
        carrello[prod] = carrello[prod] + 1
   
    # Se la chiave non esite la aggiungo con valore 1
    else:
        carrello[prod] = 1

print()
print(carrello)