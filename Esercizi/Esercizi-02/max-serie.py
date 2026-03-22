#Inizializzazione variabili
max = -1
n = -1

#Richiesta di valori in input fino a quando viene inserito 0
while n != 0:
    n = int(input("Inserire un valore positivo (0 per terminare): "))

    #Se n > max allora aggiorno il massimo
    if n > max:
        max = n


#Stampa dei risultati
print("Stampo il MASSIMO:", max)