s = input("Inserisci una stringa: ")

count = {}

for ch in s:
    if count.get(ch) == None:
        count[ch] = 1
    else:
        count[ch] += 1

print(count)