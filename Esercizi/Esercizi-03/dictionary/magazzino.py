# Inizializzazione dictionary magazzini
m1 = {"computer": 20, "frigoriferi": 6, "smartphone": 50}
m2 = {"computer": 25, "smartphone": 30, "lavatrici": 5, "lavastoviglie": 8}

# Inizializzazione dictionary di output
out = {}

# Copia di m1 in out elemento per elemento
for k in m1.keys():
    out[k] = m1[k]

# Aggiunta di valori di m2 in out
for k in m2.keys():
    
    # Controllo se il prodotto è già presente e sommo le quantità
    if(out.get(k) != None):
        out[k] = out[k] + m2[k]
    
    # Oppure aggiungo il prodotto come chiave e la sua quantità
    else:
        out[k] = m2[k]

# Stampa del risultato
print(out)