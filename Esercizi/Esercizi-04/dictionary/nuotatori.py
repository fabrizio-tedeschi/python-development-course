# Inizializzazione variabili
nuotatori = []
k = int(input("Inserire numero di nuotatori: "))
print()

for i in range(k):
    # Creo un dictionary vuoto per dati nuotatore
    n = {}

    # Aggiungo dati al dictionary
    n["nome"] = input("Inserire nome: ")
    n["cognome"] = input("Inserire cognome: ")
    n["stile"] = input("Inserire stile di nuoto: ")
    n["tempo"] = int(input("Inserire tempo in secondi: "))
    print()

    # Aggiungoil nuotatore alla lista
    nuotatori.append(n)

# Stampa dell'elenco dei nomi e dei cognomi
print("Elenco nuotatori:")
for n in nuotatori:
    print("- ", n["nome"], n["cognome"])

# Stampa dei nuotatori con tempo < 130 a rana
print()
print("Free con tempo inferiore a 98:")
for n in nuotatori:
    if n["stile"] == "Free" and n["tempo"] < 98:
        print(n["cognome"])

# Stampa dati nuotatore con tempo più basso

# Considero primo della lista come miglior nuotatore
bestn = nuotatori[0]

for n in nuotatori:
    
    # Se trovo un nuotatore con tempo migliore, lo salvo
    if(n["tempo"] < bestn["tempo"]):
        bestn = n

# Stampo i dati del nuotatore con tempo più basso
print()
print("Miglior nuotatore;")
print(bestn)