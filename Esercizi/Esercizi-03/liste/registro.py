# Inizializzazione liste vuote
cognomi = []
classi = []
medie = []

# Richiesta numero di studenti da inserire
n_stud = int(input("Numero di studenti da inserire: "))

# Inserimento dei dati di ciascun utente
for i in range(n_stud):
    print()
    cog = input("Inserire cognome: ")
    cl = input("Inserire classe: ")
    m = float(input("Inserire media: "))

    cognomi.append(cog)
    classi.append(cl)
    medie.append(m)
print()

# Scorrimento delle medie degli studenti
print("Studenti con media < 7:")
for i in range(len(medie)):

    # Se la media i-esima è inferiore a 7
    if medie[i] < 7:

        # Stampo il cognome corrispondente
        print(cognomi[i])
print()

# Richiesta di una classe
cl = input("Inserire un classe: ")

# Scorrimento di tutte le classi
for i in range(len(classi)):
    
    # Se lo studente i-esimo appartiene alla classe scelta
    if classi[i] == cl:

        # Stampo cognome e media dello studente
        print(cognomi[i], medie[i])
print()

# Richiesta di una classe
cog = input("Inserire un cognome: ")

# Controllo se il cognome esiste
if cognomi.count(cog) > 0:

    # Ricavo la posizione del cognome
    idx = cognomi.index(cog)

    # Eliminazione dei dati
    cognomi.pop(idx)
    classi.pop(idx)
    medie.pop(idx)
else:
    print("Errore: cognome inesistente!")
    
print()
print(cognomi)
print(classi)
print(medie)