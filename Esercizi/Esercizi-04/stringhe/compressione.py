s = input("Inserisci una stringa: ")

if s == "":
    print("Stringa vuota...")
else:
    compressa = ""
    precedente = s[0]
    count = 1
    for ch in s[1:]:
        if ch == precedente:
            count += 1
        else:
            compressa += precedente + str(count)
            count = 1
            precedente = ch
    compressa += precedente + str(count)
    print(compressa)