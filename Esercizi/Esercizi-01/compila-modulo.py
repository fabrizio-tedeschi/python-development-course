#Richiesta dei dati dell'utente
nome = input("Inserire il proprio nome: ")
cognome = input("Inserire il proprio cognome: ")
data_nascita = input("Inserire la propria data di nascita: ")
residenza = input("Inserire la propria residenza: ")
print()

#Inserimento dei dati nella stringa finale
out = f"Io sottoscritto {nome} {cognome} nato il {data_nascita} e residente in {residenza} mi impegno a diventare un bravo programmatore in python."
out = out.format(cognome, nome, data_nascita, residenza)

#Stampa del risultato
print(out)