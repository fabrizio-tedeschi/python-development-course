n = int(input("Inserisci n: "))

l = []
for i in range(n):
    val = int(input("Inserisci valore: "))
    l.append(val)
print(l)

minimo = min(l)
massimo = max(l)
i_min = l.index(minimo)
i_max = l.index(massimo)

t = (minimo, i_min, massimo, i_max)
print(t)