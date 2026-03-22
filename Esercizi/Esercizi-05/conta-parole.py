#Funzione per il confronto fra stringhe
def is_cointained(first, second):

    #La funzione ritorna True se la stringa first è contenuta in second
    for i in range(len(first)):
        if first[i] != second[i]:
            return False

    return True


#Apertura del file in lettura
file = open("files/secondo.txt", "r")

#Richiesta in input della parola
parola = input("Inserire la parola da cercare: ")
count = 0

#Scorro ciascuna linea del file
for line in file:

    #Il metodo split() restituisce una lista di stringhe (ossia le parole)
    for word in line.split():
        if is_cointained(parola, word):
            count += 1

print("La parola", parola, "compare", count, "volte nel file secondo.txt")