#Inizializzazione della lista
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Lista iniziale:", mylist)

#Inserimento di un elemento
mylist.append(5)

#Inserimento di un elemento in posizione 0
mylist.insert(0, 5)

#Stampa della lisat
print()
print("Lisat dopo gli inserimenti:", mylist)

#Conteggio dei numeri 5
print()
print("Nella lista sono presenti", mylist.count(5), "numeri 5")

#Rimozione della prima occorrenza di 5
print()
mylist.remove(5)
print("Lista dopo remove:", mylist)

#Utilizzo della funzione pop per rimuovere il primo elemento
print()
print("Rimosso elemento", mylist.pop(0), "che si trovava in posizione 0")
print("Lista dopo pop:", mylist)

#Ricavo l'indice della prima occorrenza di 5
print()
print("La prima occorrenza di 5 si trova in posizione", mylist.index(5))

#Stampo la lista ordinata in ordine crescente e decrescente
print()
mylist.sort()
print("Lista crescente:", mylist)
mylist.reverse()
print("Lista decrescente", mylist)