n = int(input("Inseire un numero (0 per terminare): "))

while n != 0:

    if (n % 2) == 0:
        print("Il numero", n, "risulta PARI.")
    else:
        print("Il numero", n, "risulta DISPARI.")

    n = int(input("Inseire un numero (0 per terminare): "))