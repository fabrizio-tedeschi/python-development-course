# Inizializzazione variabili
min = 0
primoval = True

# Richiesta di valori in input fino a quando viene inserito 0
while True:
    n = int(input("Inseire un numero (0 per terminare): "))

    if n == 0:
        break

    if n < min or primoval == True:
        min = n
        primoval = False

# Stampa dei risultati
print("Stampo il MINIMO:", min)