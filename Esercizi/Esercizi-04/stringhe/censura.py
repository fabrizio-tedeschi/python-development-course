frase = input("Inserisci frase: ")
c = input("Parola da censurare: ")

frase_censurata = frase.replace(c, "----")
print("Frase censurata:", frase_censurata)