#Importazione libreria random
import random

#Inizializzazione lista vuota
mylist = []

#Inserimento di numeri random
for i in range(0, 20):
    #Genrazione numero random
    val = random.randint(-50, 51)

    #Aggiunta alla lista
    mylist.append(val)

#Richiesta di un valore numerico all'utente
num = int(input("Digitare un numero compreso fra -50 e 50: "))

#Se la lista contiene almeno una occorrenza di num...
if mylist.count(num) != 0:
    print("SUCCESSO: trovata una occorrenza di", num, "nella lista!")
    print("Il valore", num, "si trova in posizione", mylist.index(num))
else:
    print("ATTENZIONE: non sono state trovate occorrenze di", num, "nella lista:")
    print(mylist)