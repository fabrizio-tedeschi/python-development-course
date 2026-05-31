prezzo = float(input("Inserisci prezzo: "))

massimo = 0
conta = 0
while prezzo != 0:
    if prezzo > massimo:
        conta = 1
        massimo = prezzo
    elif prezzo == massimo:
        conta += 1
    
    prezzo = float(input("Inserisci prezzo: "))

print("Prezzo massimo:", massimo)
print("Numero negozi che applicano prezzo massimo:", conta)
