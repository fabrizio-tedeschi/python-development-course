n_piatto = int(input("Inserire il numero del piatto: "))
pezzi = int(input("Inserire numero pezzi: "))
servizio = input("Servizio al tavolo? (si/no): ")

match n_piatto:
    case 1:
        prezzo = 6
    case 2:
        prezzo = 7
    case 3:
        prezzo = 5
    case 4:
        prezzo = 9
    case 5:
        prezzo = 4
    case _:
        print("Piatto inesistente: ordinerai una pizza!")
        prezzo = 6

print("Calcolo il costo in base ai pezzi...")
costo_ordine = prezzo*pezzi

if servizio == "si":
    persone = int(input("Inserisci numero persone: "))
    
    print("Calcolo il supplemento a persona...")
    costo_ordine += persone*2

if pezzi > 8:
    print("Applico sconto 20%...")
    sconto = costo_ordine/100*20
    costo_ordine -= sconto
elif prezzo > 4:
    print("Applico sconto 10%...")
    sconto = costo_ordine/100*10
    costo_ordine -= sconto

print()
print("Totale ordine:", costo_ordine)