n = int(input("Inserisci n: "))

persone = []
for i in range(n):
    nome = input("Inserisci nome: ")
    eta = int(input("Inserisci eta: "))
    pers = (nome, eta)
    persone.append(pers)

print(persone, "\n")

giovane = persone[0]
for p in persone:
    if p[1] < giovane[1]:
        giovane = p
print("Persona piu giovane:", giovane)

somma = 0
for p in persone:
    somma += p[1]
media = somma/len(persone)
print("Eta media:", round(media, 2))