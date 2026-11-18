frase = input("Inserisci frase: ")
parole = frase.split(" ")

max_parola = parole[0]
max_len = len(parole[0])

for p in parole:
    if len(p) > max_len:
        max_len = len(p)
        max_parola = p

print(f"Parola massima: {max_parola} ({max_len} caratteri)")