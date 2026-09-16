s1 = input("Inserisci una stringa: ")
s1 = s1.replace(" ", "")

chars = list(s1)
chars.reverse()
s2 = "".join(chars)

if s1 == s2:
    print("Palindromo!")
else:
    print("Non palindromo :(")