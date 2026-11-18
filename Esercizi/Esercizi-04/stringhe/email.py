email = input("Inserisci indirizzo email: ")
valido = True

parti = email.split("@")

if len(parti) != 2:
    print("ERRORE: carattere @.")
    valido = False
else:
    utente = parti[0]
    dominio = parti[1]

    if utente == "" or dominio == "":
        print("ERRORE: utente o dominio vuoti.")
        valido = False

    if "." not in dominio:
        print("ERRORE: dominio non valido.")
        valido = False

if valido:
    print("Indirizzo valido")
    print("Utente:", utente)
    print("Dominio:", dominio)
else:
    print("Indirizzo non valido.")