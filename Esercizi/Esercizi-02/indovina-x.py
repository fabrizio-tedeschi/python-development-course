import random
x = random.randint(0, 20)

n = int(input("Inserisci numero: "))
while n != x:
    if n > x:
        print("Troppo alto...")
    elif n < x:
        print("Troppo basso...")

    n = int(input("Inserisci numero: "))

print("Indovinato!")