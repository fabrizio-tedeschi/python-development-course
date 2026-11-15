def posizioni(l, e):
    out = []
    for i in range(len(l)):
        if l[i] == e:
            out.append(i)
    return out

l = [4, 7, 4, 1, 4]
e = 4
out = posizioni(l, e)
print(f"Chiamo posizioni({l}, {e})...")
print(f"La funzione ha ritornato: {out}")

l = []
e = 4
out = posizioni(l, e)
print(f"Chiamo posizioni({l}, {e})...")
print(f"La funzione ha ritornato: {out}")

l = [4, 7, 4, 1, 4]
e = 6
out = posizioni(l, e)
print(f"Chiamo posizioni({l}, {e})...")
print(f"La funzione ha ritornato: {out}")