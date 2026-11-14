g1 = int(input("Inserisci giorno: "))
m1 = int(input("Inserisci mese: "))
a1 = int(input("Inserisci anno: "))
data_1 = (a1, m1, g1)

g2 = int(input("Inserisci giorno: "))
m2 = int(input("Inserisci mese: "))
a2 = int(input("Inserisci anno: "))
data_2 = (a2, m2, g2)

if data_1 == data_2:
    print("Stessa data.")
elif data_1 > data_2:
    print("Piu recente:", data_1)
else:
    print("Piu recente:", data_1)