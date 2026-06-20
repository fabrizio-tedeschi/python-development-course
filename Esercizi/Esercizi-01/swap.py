import random

a = random.randint(5, 15)
b = random.randint(5, 15)
print("a =", a, "b =", b)

print("Scambio le variabili...")
tmp = a
a = b
b = tmp

print("a =", a, "b =", b)