def aggiungi(rubrica, nome, telefono):
    if nome in rubrica:
        return False
    else:
        rubrica[nome] = telefono
        return True

def cerca(rubrica, nome):
    if nome in rubrica:
        return rubrica[nome]
    else:
        return None

def elimina(rubrica, nome):
    if nome in rubrica:
        del rubrica[nome]
        return True
    else:
        return False

rub = {}

for i in range(4):
    nome = input("Inserisci nome: ")
    num = input("inserisci numero: ")
    if aggiungi(rub, nome, num):
        print("Contatto aggiunto!")
    else:
        print("Errore: contatto gia presente!")

cercato = input("Inserisci nome da cercare: ")
out = cerca(rub, nome)
if out == None:
    print("Errore: contatto non trovato!")
else:
    print(f"Numero di {cercato}: {out}")

rimuovendo = input("Inserisci nome contatto da rimuovere: ")
if not elimina(rub, rimuovendo):
    print("Errore: contatto non trovato!")
else:
    print(rub)