print("Calcolo prezzo di noleggio bici")
elettrica = input("La bici è elettrica? (si/no): ")
studente = input("Sei uno studente? (si/no): ")
ore = int(input("Numero di ore di noleggio: "))

costo_base = 5

print("Calcolo il costo in base alle ore...")
costo = costo_base + 2.5*ore

if elettrica == "si":
    print("Aggiungo il supplemento per bici elettriche...")
    costo += 8

if studente == "si":
    print("Applico lo sconto studente...")
    sconto = costo/100*15
    costo -= sconto

if ore > 6:
    print("Applico lo sconto per ore >6...")
    sconto = costo/100*10
    costo -= sconto
elif ore > 3:
    print("Applico lo sconto per ore >3...")
    sconto = costo/100*25
    costo -= sconto

costo = round(costo, 2)
print("Costo finale:", costo)