import pandas as pd

# Input dati
th = int(input("Inserisci una soglia: "))

l = []
for i in range(10):
    n = int(input("Inserisci numero: "))
    l.append(n)

# Creazione della series
s = pd.Series(l)
print()
print(s)

# Estrazione dei soli valori maggiori della soglia
s2 = s[s > th]
print()
print(s2)