#Input delle cifre (partendo da sinistra)
centinaia = input("Inseire la cifra delle centinaia: ")
decine = input("Inseire la cifra delle decine: ")
unita = input("Inseire la cifra delle unita: ")
print()

#Creazione della numero (stringa)
num = centinaia + decine + unita

#Trasformazione della stringa in intero
num = int(num)

#Stampa del numero moltiplicato per 10
print("Risultato finale: ", num * 10)