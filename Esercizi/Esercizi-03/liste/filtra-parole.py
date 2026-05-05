# Inizializzazione liste
parole = ["alfabeto", "insuperabile", "", "infinito", "icaro"]
filtered = []

# Scorro tutte le parole della lista
for p in parole:

    # Se una parola ha come primi due carateri "in"
    if p[0:2] == "in":

        # Aggiungo la parola alla lista
        filtered.append(p)

# Stampa della lista finale
print(filtered)