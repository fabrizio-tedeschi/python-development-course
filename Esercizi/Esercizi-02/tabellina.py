n = int(input("Inserisci un numero: "))

while n < 0:
    print("Il numero deve essere non negativo!")
    n = int(input("Inserisci un numero: "))

print("Elenco divisiori di n =", n)
for i in range(11):
    res = n*i
    print(f"{n} x {i} = {res}")
