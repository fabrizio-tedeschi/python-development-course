#Inizializzazione di una lista
lista = [10, 20, 30, 40, 50, 60, 70, 80, 90]

#Iterazione tramite elementi
print()
print("Inizio iterazione sulla lista tramite elementi:")

#Inizializzazione dell'indice progressivo di posizione
index = 0

for elemento in lista:
    print("Stampo l'elemento corrente:", elemento)
    print("L'elemento si trova in posizione", index)

    #Aggiornamento dell'indice
    index += 1

#Iterazione tramite indice
print()
print("Inizio iterazione sulla lista tramite indice:")

#Ricavo la lunghezza della lista
lunghezza = len(lista)

for i in range(0, lunghezza):
    print("Stampo l'elemento corrente:", lista[i])
    print("L'elemento si trova in posizione", i)