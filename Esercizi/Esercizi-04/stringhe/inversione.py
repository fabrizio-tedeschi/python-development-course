s = input("Inserisci una stringa: ")

r = ""
for i in range(len(s)):
    ch = s[(-i-1)]
    r += ch

print(r)