#Definizione di una prima lista
l1 = [1, 2, 3, 4, 5]

print()
print("Lista iniziale l1:", l1)
print()

#Assegnazione: l1 ed l2 sono riferimenti alla stessa lista
print("Copio il riferimento di l1 in l2...")
print()
l2 = l1

#La rimozione di un elemento da l1 la provoca anche in l1
print("Rimuovo il primo elemento di l1...")
l1.pop(0)

print("Lista 1:", l1)
print("Lista 2:", l2)
print()

#Copia della lista l1 in l3
print("Copio l1 in l3...")
print()
l3 = l1.copy()

#La rimozione di un elemento da l1 la provoca anche in l1
print("Rimuovo il primo elemento di l1...")
l1.pop(0)

print("Lista 1:", l1)
print("Lista 3:", l3)
print()