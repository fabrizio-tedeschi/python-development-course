s = input("Inserisci una stringa: ")

count = 0
for ch in s:
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
        count += 1

print("Numero vocali:", count)