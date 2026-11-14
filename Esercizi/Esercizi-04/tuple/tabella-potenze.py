n = int(input("Inserisci numero intero positivo n: "))

print("Tabella potenze:")
print("(num, quadrato, cubo)")
for i in range(n):
    t = (i, i**2, i**3)
    print(t)