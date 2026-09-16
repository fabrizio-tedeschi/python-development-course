def filtra_nomi(l, ch):
    out = []
    for nome in l:
        if nome[0] == ch:
            out.append(nome)
    return out

nomi = ["mario", "anna", "marco", "luigi", "angela"]

r = filtra_nomi(nomi, "a")
print("Nomi che inziiano per a:", r)

r = filtra_nomi(nomi, "m")
print("Nomi che inziiano per m:", r)

r = filtra_nomi(nomi, "l")
print("Nomi che inziiano per l:", r)

r = filtra_nomi(nomi, "f")
print("Nomi che inziiano per f:", r)