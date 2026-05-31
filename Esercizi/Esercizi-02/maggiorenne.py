nome = input("Inserire il proprio nome: ")
cognome = input("Inserire il proprio cognome: ")
anni = int(input("Inserire i propri anni: "))
print()

print("Ciao", nome, cognome)

if anni >= 18:
    print("Sei maggiorenne, BENVENUTO!")
else:
    print("Sei minorenne, ACCESSO NEGATO!")