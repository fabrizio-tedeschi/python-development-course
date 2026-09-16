s = input("Inserisci una stringa: ")

count = 0
for ch in s:
    if ch == " ":
        count += 1

if s != "":
    count += 1

print("Numero parole:", count)