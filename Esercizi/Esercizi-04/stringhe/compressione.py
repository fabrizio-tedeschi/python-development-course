s = input("Inserisci una stringa: ")

compressa = ""
precedente = s[0]
count = 1
for i in range(1, len(s)):
    if s[i] == precedente:
        count += 1
    else:
        compressa += precedente
        compressa += str(count)
        count = 1
        precedente = i

print(compressa)