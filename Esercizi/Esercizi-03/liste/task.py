# Inizializzazione delle liste vuote
tasks = []

# Input della lunghezza della lista
n = int(input("Numero di task da inserire: "))

# Inserimento dei prodotti
for i in range(n):
    t = input("Inserire un task: ")
    tasks.append(t)

# Eliminazione di un task per indice
idx = int(input("Inserire indice di un task da eliminare: "))
popped = tasks.pop(idx)
print("Eliminato task", popped)

# Eliminazione di un task per nome
t = input("Inserire il nome di un task da eliminare: ")

if tasks.count(t) > 0:
    tasks.remove(t)
else:
    print("ERRORE: task inesistente")
    
# Stampa finale della lista dei task
print()
print("Lista dei task restanti:")

for i in range(len(tasks)):
    print("-", tasks[i])