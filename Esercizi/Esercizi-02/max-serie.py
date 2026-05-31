max = -1
n = -1

while n != 0:
    n = int(input("Inserire un valore positivo (0 per terminare): "))

    if n > max:
        max = n


print("Stampo il MASSIMO:", max)