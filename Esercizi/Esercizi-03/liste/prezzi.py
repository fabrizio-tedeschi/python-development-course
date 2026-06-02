import random
n = int(input("Numero di prodotti da inserire: "))

prodotti = []
for i in range(n):
    p = input("Inserire nome prodotto: ")
    while p == "":
        print("Nome prodotto non valido!")
        p = input("Inserire nome prodotto: ")
    prodotti.append(p)

prezzi = []
for i in range(n):
    x = random.randint(20, 300)
    prezzi.append(x)

for i in range(n):
    if prezzi[i] < 50:
        print("-", prodotti[i], prezzi[i], "Fascia: BASSA")
    elif prezzi[i] < 150:
        print("-", prodotti[i], prezzi[i], "Fascia: MEDIA")
    else:
        print("-", prodotti[i], prezzi[i], "Fascia: ALTA")