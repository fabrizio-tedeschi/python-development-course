# Lista iniziale di ordini
ordini = [
    {"id": 1, "cliente": "Marco", "spesa": 250, "pagato": True},
    {"id": 2, "cliente": "Anna", "spesa": 120, "pagato": False},
    {"id": 3, "cliente": "Marco", "spesa": 75, "pagato": True},
    {"id": 4, "cliente": "Luca", "spesa": 310, "pagato": False},
    {"id": 5, "cliente": "Anna", "spesa": 90, "pagato": True}
]

# Variabile somma delle spese
tot = 0

# Scorro un ordine per volta
for ord in ordini:

    # Ricavo la spesa dell'ordine e la sommo al totale solo se l'ordine è stato pagato
    if ord["pagato"] == True:
        tot += ord["spesa"]

print("Incasso totale:", tot)

# Dictionary vuoto per le spese di ogni cliente
spese = {}

# Scorro un ordine per volta
for ord in ordini:

    # Ricavo il nome del cliente
    nome = ord["cliente"]

    # Controllo se il nome del cliente non esiste
    if spese.get(nome) == None:
        # Aggiungo il nome del cliente e la spesa
        spese[nome] = ord["spesa"]
    else:
        # Aggiorno la spesa del cliente esistente
        spese[nome] += ord["spesa"]

print(spese)

# Lista vuota per ordini non pagati
nonpagati = []

# Scorro un ordine per volta
for ord in ordini:

    # Se l'ordine non è pagato
    if ord["pagato"] == False:
        # Lo aggiungo alla lista dei non pagati
        nonpagati.append(ord)

print(nonpagati)