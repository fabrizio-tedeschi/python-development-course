n = int(input("Numero di prodotti da inserire: "))

magazzino = {}
for i in range(n):
    prod = input("Nome prodotto: ")
    qt = int(input("Quantita: "))
    pz = float(input("Prezzo: "))
    magazzino[prod] = {"quantita": qt, "prezzo": pz}
print(magazzino)

print("Prodotti sottoscorta:")
for k, v in magazzino.items():
    if v["quantita"] < 5:
        print("-", k)

valore_magazzino = 0
for k, v in magazzino.items():
    valore_magazzino += v["quantita"]*v["prezzo"]
print("Valore magazzino:", valore_magazzino)

nome = input("Nome del prodotto venduto: ")
qt = int(input("Quantita venduta: "))

if nome not in magazzino:
    print("Errore: prodotto inesistente!")
elif magazzino[nome]["quantita"] < qt:
    print("Errore: pezzi non sufficienti!")
else:
    magazzino[nome]["quantita"] -= qt
    print("Vendita effettuata correttamente!")

print(magazzino)