import random

l = []
for i in range(10):
    x = random.randint(-50, -20)
    l.append(x)
print(l)

massimo = l[0]
minimo = l[0]
for num in l:
    if num > massimo:
        massimo = num
    if num < minimo:
        minimo = num
    
print("Massimo:", massimo)
print("Minimo:", minimo)

"""
In alternativa al ciclo for:
massimo = max(l)
minimo = min(l)
"""