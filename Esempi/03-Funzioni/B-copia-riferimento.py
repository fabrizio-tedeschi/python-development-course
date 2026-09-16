#Definizione della funzione che accetta il parametro x per copia
def aggiungi(x):
    return x + 10                           #Ritorna: x + 10

#Definizione della funzione che accetta lista per riferimento ed elemento per copia
def aggiungi_elemento(lista, elemento):
    lista.append(elemento)                  #Aggiunge l'elemento alla lista l
    return lista                            #Ritorna un nuovo riferimento alla lista l

#Inizializzazione variabili per test
var = 15
l = [1, 2, 3]

#Test su parametro passato per copia
res = aggiungi(var)
print(var)                                  #Stampa: 15
print(res)                                  #Stampa: 25

#Test su parametro passato per riferimento
risultato = aggiungi_elemento(l, 4)
risultato.append(5)
print(l)                                    #Stampa: [1, 2, 3, 4, 5]
print(risultato)                            #Stampa: [1, 2, 3, 4, 5]