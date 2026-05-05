# Inizializzazione della lista
nuotatori = [
    {"nome": "Mario", "cognome": "Rossi", "stile": "Rana", "tempo": 125},
    {"nome": "Luigi", "cognome": "Verdi", "stile": "Free", "tempo": 95},
    {"nome": "Anna", "cognome": "Bianchi", "stile": "Free", "tempo": 80},
    {"nome": "Giulia", "cognome": "Monti", "stile": "Free", "tempo": 100},
]

# Ricavo la lunghezza della lista
k = len(nuotatori)

# Ordinamento della lista per minor tempo
for i in range(k):
    for j in range(i+1, k):
        if nuotatori[j]["tempo"] < nuotatori[i]["tempo"]:
            tmp = nuotatori[i]
            nuotatori[i] = nuotatori[j]
            nuotatori[j] = tmp

# Stampa della classifica
print("\nClassifica generale:")

count = 1
for n in nuotatori:
    print(str(count)+".", n["cognome"], "-", n["tempo"], "-", n["stile"])
    count += 1

# Stampa classifica solo Free
print("\nClassifica stile libero:")

count = 1
for n in nuotatori:
    if n["stile"] == "Free":
        print(str(count)+".", n["cognome"], "-", n["tempo"], "-", n["stile"])
        count += 1