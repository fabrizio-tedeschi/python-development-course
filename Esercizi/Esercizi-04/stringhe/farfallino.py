frase = input("Inserire una frase: ")
frase = frase.lower()

traduzione = ""

for ch in frase:
    if ch in "aeiou":
        traduzione += ch + "f" + ch
    else:
        traduzione += ch

print("Frase tradotta:", traduzione)