from random import randint
from random import choice

#Inizializzazione liste
senders = []
blacklist = []
received = []

#Generazione indirizzi IP
for i in range(0, 20):
    IP = "{}.{}.{}.{}".format(
        randint(0, 255),
        randint(0, 255),
        randint(0, 255),
        randint(0, 255)
    )
    senders.append(IP)

#Esecuzione del programma
for i in range(0, 60):

    #Scelta di un indirizzo IP casuale fra quelli generati
    IP = choice(senders)

    #Aggiunta dell'indirizzo IP alla lista di quelli ricevuti
    received.append(IP)

    #Controllo delle richieste effettuate dall'IP
    if received.count(IP) >= 4:
        if blacklist.count(IP) < 1:
            blacklist.append(IP)
    else:
        print("Fornita risposta ad indirizzo IP:", IP)

#Stampa delle liste
print()
print("La lista senders contiene", len(senders), "elementi:")
print(senders)
print()
print("La blacklist contiene", len(blacklist), "elementi:")
print(blacklist)