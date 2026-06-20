centinaia = input("Inseire la cifra delle centinaia: ")
decine = input("Inseire la cifra delle decine: ")
unita = input("Inseire la cifra delle unita: ")
print()

# Creazione della numero (stringa) e conversione
num = centinaia + decine + unita
num = int(num)

print("Numero: ", num)
print("Risultato finale: ", num / 2)

# Soluzione alternativa
centinaia = int(centinaia)
decine = int(decine)
unita = int(unita)
num = centinaia*100 + decine*10 + unita