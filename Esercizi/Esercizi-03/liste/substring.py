# Inizializzazione delle liste
parole = ["mare", "solemarenuvole", "", "spiaggia", "amarene"]
filtered = []
searched = "mare"

# Scorrimento della lista di parole
for p in parole:

    # Se la parola cercata è sottostringa di p
    if searched in p:

        # Aggiungo p alla lista finale
        filtered.append(p)

# Stampa della lisat finale
print(filtered)