frase = input("Inserisci frase: ")
c = input("Parola da censurare: ")

quanti = len(c)
frase_censurata = frase.replace(c, ("-"*quanti))
print("Frase censurata:", frase_censurata)