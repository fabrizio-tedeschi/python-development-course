n = int(input("Numero di citta da inserire: "))

# Input e costruzione dictionary
d = {}
for i in range(n):
    c = input("Inserire città: ")
    p = int(input("Inserire popolazione: "))
    d[c] = p
print(d)

# Ricerca città popolazione massima e minima

cmax = ""
pmax = 0
for c in d.keys():
    if d[c] >= pmax:
        pmax = d[c]
        cmax = c
print("Città con popolazione piu alta:", cmax)

cmin = ""
pmin = d[c]
for c in d.keys():
    if d[c] <= pmin:
        pmin = d[c]
        cmin = c
print("Città con popolazione piu bassa:", cmin)

# Media popolazione

somma = 0
conta = 0
for val in d.values():
    somma += val
    conta += 1
media = somma / conta
media = round(media, 2)
print("Popolazione media:", media)