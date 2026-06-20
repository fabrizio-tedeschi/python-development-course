anni = int(input("Quanti hanni hai? "))
n_mesi = int(input("Quanti mesi di abbonamento desideri? "))

costo_mese = 30
costo_assicurazione = 10

print("Calcolo prezzo base...")
prezzo = costo_mese * n_mesi

if anni < 18:
    print("Aggiungo assicurazione...")
    prezzo += costo_assicurazione
elif anni < 20 or anni > 60:
    print("Applico sconto giovani/anziani...")
    sconto = prezzo / 100 * 20
    prezzo -= sconto

if n_mesi >= 8:
    print("Applico sconto mesi >8...")
    sconto = prezzo / 100 * 40
    prezzo -= sconto
elif n_mesi >= 4:
    print("Applico sconto mesi >4...")
    sconto = prezzo / 100 * 30
    prezzo -= sconto

print("Totale da pagare:", prezzo)