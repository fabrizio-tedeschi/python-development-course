cognomi = []
squadre = []
valori_mercato = []

print("GESTIONE GIOCATORI")
print("1) Inserisci giocatori")
print("2) Filtra per squadra")
print("3) Soglia valori")
print("4) Media squadra")
print("5) USCITA")

comando = int(input("Inserisci un comando [1-5]: "))

while comando != 5:
    
    if comando == 1:
        n = int(input("Numero di giocatori da inserire: "))
        for i in range(n):
            cognome = input("Inserire nome giocatore: ")
            squadra = input("Inserire squadra giocatore: ")
            valore = int(input("Inserire valore di mercato giocatore: "))

            cognomi.append(cognome)
            squadre.append(squadra)
            valori_mercato.append(valore)

    elif comando == 2:
        sq = input("Inserire la squadra da cercare: ")
        if squadre.count(sq) == 0:
            print("ERRORE: squadra inesistente!")
        else:
            for i in range(len(squadre)):
                if squadre[i] == sq:
                    print(cognomi[i])

    elif comando == 3:
        s = int(input("Inserire una soglia (> 500): "))
        while s < 500:
            s = int(input("Inserire una soglia (> 500): "))
        
        for i in range(len(valori_mercato)):
            if valori_mercato[i] > s:
                print(cognomi[i], squadre[i])

    elif comando == 4:
        sq = input("Inserire la squadra da cercare: ")
        if squadre.count(sq) == 0:
            print("ERRORE: squadra inesistente!")
        else:
            cont = 0
            somma = 0
            for i in range(len(valori_mercato)):
                if squadre[i] == squadra:
                    somma += valori_mercato[i]
                    cont += 1
            media = somma/cont
            print(f"Valore medio di mercato di {sq}:", media)

    elif comando == 5:
        print("Uscita dal programma...")
    else:
        print("Comando non valido")
    
    comando = int(input("Inserisci un comando [1-5]: "))