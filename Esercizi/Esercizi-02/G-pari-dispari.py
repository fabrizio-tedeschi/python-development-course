# Richiesta di valori in input fino a quando viene inserito 0
while True:
    n = int(input("Inseire un numero (0 per terminare): "))

    if n == 0:
        break

    if (n % 2) == 0:
        print("Il numero", n, "risulta PARI.")
    else:
        print("Il numero", n, "risulta DISPARI.")