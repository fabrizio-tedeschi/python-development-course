def intersezione(l1, l2):
    out = []
    for e in l1:

        # Se l'elemento è presente sia in l1 sia in l2 e non lo ho già inserito
        if l2.count(e) >= 1 and out.count(e) == 0:
            out.append(e)
    return out

l1 = [1, 2, 3, 4, 5, 5, 6]
l2 = [4, 5, 6, 7, 8, 9, 10]

out = intersezione(l1, l2)
print("Intersezione:", out)