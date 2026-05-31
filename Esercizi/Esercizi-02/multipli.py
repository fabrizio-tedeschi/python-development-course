x = int(input("Inserisci numero x: "))

while x <= 0:
    print("Il numero deve essere positivo!")
    x = int(input("Inserisci numero x: "))

conta = 0
n = int(input("Inserisci numero (0 per terminare): "))

while n != 0:
    if n % x == 0:
        conta += 1

    n = int(input("Inserisci numero (0 per terminare): "))

print("I multipli di", x, "sono", conta)