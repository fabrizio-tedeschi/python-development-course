#Input dei dati
nome = input("Inserire il proprio nome: ")
cognome = input("Inserire il proprio cognome: ")
anni = int(input("Inserire i propri anni: "))
print()

#Stampa del risultato su output
print("Ciao", nome, cognome)

#Controllo degli anni
if anni >= 18:
    print("Sei maggiorenne, BENVENUTO!")
else:
    print("Sei minorenne, ACCESSO NEGATO!")