def filtra_parole(l, s):
    out = []
    n = len(s)
    for parola in l:
        if parola[:n] == s:
            out.append(parola)
    return out

parole = ["ciao", "mare", "maestro", "maestrale", "cesto", "canestro", "cestino"]

r = filtra_parole(parole, "c")
print("Parole che inziiano per c:", r)

r = filtra_parole(parole, "ma")
print("Parole che inziiano per ma:", r)

r = filtra_parole(parole, "ces")
print("Parole che inziiano per ces:", r)

r = filtra_parole(parole, "boh")
print("Parole che inziiano per boh:", r)