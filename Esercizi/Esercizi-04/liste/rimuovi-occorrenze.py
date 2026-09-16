#Definizione della funzione
def rimuovi_occorrenze(l, e):
    out = []
    for i in l:
        if i != e:
            out.append(i)
    return out

#Istruzioni di test
lista = [1, "parola", 2, 5, False, 7, 5, 15]

print("Lista iniziale:", lista)
print()
print(rimuovi_occorrenze(lista, 5))
print(rimuovi_occorrenze(lista, "s"))
print(rimuovi_occorrenze(lista, False))