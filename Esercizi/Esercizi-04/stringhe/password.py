psw = input("Imposta una password: ")

check_lunghezza = False
check_minuscola = False
check_maiuscola = False
check_cifra = False

if len(psw) >= 8:
    check_lunghezza = True

for ch in psw:
    if ch.isdecimal():
        check_cifra = True

    if ch.islower():
        check_minuscola = True
    
    if ch.isupper():
        check_maiuscola = True

if check_lunghezza and check_minuscola and check_maiuscola and check_cifra:
    print("Password sicura :)")
else:
    print("Password debole :(")    