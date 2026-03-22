#Apertura del file
file = open("files/primo.txt", "r")

#Lettura e stampa delle prime 10 linee
print("Mosto le prime 10 linee de file primo.txt:")

for i in range(0, 10):
    #Lettura della linea
    line = file.readline()

    #Stampa della linea ed eliminazione del terminatore
    print(line.replace("\n", ""))
