nome_snake = input("Inserisci nome in snake_case: ")

if nome_snake == "":
    print("Stringa vuota...")
else:
    parole = nome_snake.split("_")
    nome_camel = ""
    for p in parole:
        pnew = p[0].upper() + p[1:]
        nome_camel += pnew

    print("CamelCase:", nome_camel)