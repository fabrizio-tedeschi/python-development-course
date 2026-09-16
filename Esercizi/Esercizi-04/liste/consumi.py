import random

n = 12
produzione = []
consumi = []

for i in range(n):
    p = random.randint(0, 15)
    c = random.randint(2, 10)

    produzione.append(p)
    consumi.append(c)
print("Produzione:", produzione)
print("Consumi:", consumi)
print()

for i in range(n):
    if produzione[i] > consumi[i]:
        print("Ora", i, "RISPAMIO")
    elif produzione[i] < consumi[i]:
        print("Ora", i, "CONSUMO")
    else:
        print("Ora", i, "IMPATTO ZERO")