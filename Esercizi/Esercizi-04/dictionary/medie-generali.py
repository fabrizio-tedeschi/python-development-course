medie = {}
n = int(input("Studenti da inserire: "))

for i in range(n):
    cognome = input("Inserire cognome: ")
    media = float(input("Inserire media: "))
    medie[cognome] = media

print(medie)
c = input("Inserire un cognome da cercare: ")

if medie.get(c) == None:
    print("ERRORE: cognome inesistente!")
else:
    print(medie[c])