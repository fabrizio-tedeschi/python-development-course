# Inizializzazione delle liste vuote
lista = []
qt = []

# Input della lunghezza della lista
n = int(input("Numero di prodotti da inserire: "))

# Inserimento dei prodotti
for i in range(n):
    prod = input("Inserire un prodotto: ")
    lista.append(prod)

# Ordinamento dei prodotti in ordine alfabetico
lista.sort()

# Richiesta delle quantità
for i in range(n):
    print("Inseire la quantità desiderata per", lista[i])
    q = int(input("Quantita: "))
    qt.append(q)

# Stampa finale della lista della spesa
print()
print("Lista della spesa finale:")

for i in range(n):
    print("-", lista[i], qt[i])