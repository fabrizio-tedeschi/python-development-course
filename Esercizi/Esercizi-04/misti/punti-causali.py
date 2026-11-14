import random

punti = []
for i in range(8):
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    p = (x, y)
    punti.append(p)

print(punti, "\n")

print("Punti del primo quadrante:")
for p in punti:
    if p[0] > 0 and p[1] > 0:
        print(p)