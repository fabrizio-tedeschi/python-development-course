n = int(input("Inserisci un numero: "))

while n < 0:
    print("Il numero deve essere non negativo!")
    n = int(input("Inserisci un numero: "))

for i in range(1, n+1):
    print(i * "*")