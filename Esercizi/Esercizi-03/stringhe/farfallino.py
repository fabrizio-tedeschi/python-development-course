frase = input("Inserire una frase: ")
frase = frase.lower()

traduzione = ""

for ch in frase:
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
        traduzione += ch + "f" + ch
    else:
        traduzione += ch

print("Frase tradotta:", traduzione)