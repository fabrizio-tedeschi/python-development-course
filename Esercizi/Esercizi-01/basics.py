x = int(input("Inserisci valore di x: "))
y = int(input("Inserisci valore di y: "))

print("x =", x, "y =", y)
print()

print("Incremento x...")
x = x + 20
print("x =", x, "y =", y)

diff = x - y
print("x-y =", diff)
print()

print("Decremento y...")
y = y - 4
print("x =", x, "y =", y)

s = x + y
print("x+y =", s)
print()

resto = x % y
print("Resto di x/y:", resto)
print()

pot = x**y
print("Potenza x^y:", pot)