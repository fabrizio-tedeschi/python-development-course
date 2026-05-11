# Input dei dati
anni = int(input("Quanti hanni hai? "))
n_mesi = int(input("Quanti mesi di abbonamento desideri? "))

# Calcolo del prezzo
costo_mese = 30
costo_assicurazione = 10

prezzo = costo_mese * n_mesi

if anni < 18:
    prezzo += costo_assicurazione
elif anni < 20 or anni > 60:
    sconto = prezzo / 100 * 20
    prezzo -= sconto

if n_mesi >= 8:
    sconto = prezzo / 100 * 40
    prezzo -= sconto
elif n_mesi >= 4:
    sconto = prezzo / 100 * 30
    prezzo -= sconto

# Stampa del risultato
print("Totale da pagare:", prezzo)