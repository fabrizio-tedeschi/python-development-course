#Apertura del file su cui scrivere
fout = open("files/print-out.txt", "w")

for i in range(0, 10):

    #Lettura di una linea inserita dall'utente
    line = input("Inseire la linea " + str(i+1) + ": ")

    #Aggiunta del terminatore alla linea
    line += "\n"

    #Scrittura della linea su file
    fout.write(line)