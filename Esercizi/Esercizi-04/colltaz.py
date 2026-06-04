import random

def colltaz(x):
    out = []

    if x <= 0:
        return out

    while x != 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3*x + 1

        out.append(x)

    return out

numeri = []
for i in range(5):
    n = random.randint(-10, 30)
    numeri.append(n)

for n in numeri:
    successione = colltaz(n)
    print(n, "-->", successione)