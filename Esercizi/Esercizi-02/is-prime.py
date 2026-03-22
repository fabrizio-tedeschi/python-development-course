#Input di un numero intero
x = int(input("Inseire un numero: "))

#Inizializzazione di una variabile di controllo
primo = True

#Scorro tutti i valori da 2 fino ad x escluso
for i in range(2, x):
    #Se il numero è divisibile per uno di questi valori...
    if x % i == 0:
        #...il numero non è primo
        primo = False
        #Non sono necessari ulteriori controlli: posso interrompere il ciclo
        break

if primo:
    print("Il numero", x, "risulta PRIMO!")
else:
    print("Il numero", x, "NON risulta primo!")