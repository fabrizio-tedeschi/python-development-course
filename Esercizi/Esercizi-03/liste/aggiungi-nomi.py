#Inizializzazione della lista vuota
nomi = []

#Iterazione su range (da 0 a 4)
for i in range(0, 5):

    #Richiesta all'utente del nome da inserire
    n = input("Inserire un nome: ")

    #Inserimento del nome nella lista
    nomi.append(n)

    #Stampa del messaggio di debug
    print("DEBUG - inserito nome in posizione", i)

#Stampa della lista ottenuta
print()
print(nomi)