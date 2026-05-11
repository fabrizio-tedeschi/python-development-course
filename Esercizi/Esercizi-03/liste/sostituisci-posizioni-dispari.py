#Inizializzazione della lista
l = ["Mario", 15, "Luigi", 16, "Bianca", 20, "Rosa", 15, "Anna", 20]

#Inizializzazione di un contatore per l'indice di posizione
i = 0

#Scorrimento della lista
for e in l:

    #In caso di indice dispari (l'elemento corrente è un numero)
    if i % 2 != 0:

        #Rimozione dell'elemento all'indice corrente e stampa di debug
        popped = l.pop(i)
        print("DEBUG - rimosso elemento:", popped)

        #Inserimento della stringa vuota al posto dell'elemento rimosso
        l.insert(i, "")

    #Aggiornamento dell'indice di posizione
    i += 1

#Stampa della lista rimanente
print()
print("Lista senza interi:", l)