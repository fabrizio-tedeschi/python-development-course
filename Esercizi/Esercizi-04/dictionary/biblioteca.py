n = int(input("Numero libri da inserire: "))

libri = {}
for i in range(n):
    isbn = input("Inserisci ISBN: ")
    prestiti = int(input("Inserisci numero prestiti: "))
    libri[isbn] = prestiti
print(libri)

print("Libri mai prestati:")
for k, v in libri.items():
    if v == 0:
        print("-", k)

totale_prestiti = sum(list(libri.values()))
print("Totale prestiti:", totale_prestiti)

guadagno = totale_prestiti * 0.5
print("Guadagno mensile:", guadagno)

codice = input("Inserisci libro da cercare: ")
if codice in libri:
    print(f"Libro prestato {libri[codice]} volte.")
else:
    print("Codice non valido!")