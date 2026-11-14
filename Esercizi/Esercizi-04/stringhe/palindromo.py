s1 = input("Inserisci una stringa: ")
s1 = s1.replace(" ", "")
s1 = s1.lower()

# Reverse string
s2 = s1[::-1]

if s1 == s2:
    print("Palindromo!")
else:
    print("Non palindromo :(")