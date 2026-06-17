import random

print("BENVENUTO AI MINIGIOCHI")
print()
print("1) Indovina x")
print("2) Gara tabelline")
print("3) Indovina x difficile")

comando = int(input("Inserire comando: "))

while comando != 4:

    if comando == 1:
        x = random.randint(0, 20)
        n = int(input("Inserisci numero: "))
        while n != x:
            if n > x:
                print("Troppo alto...")
            elif n < x:
                print("Troppo basso...")

            n = int(input("Inserisci numero: "))
        print("Indovinato!")

    elif comando == 2:
        count = 0
        for i in range(5):
            x = random.randint(0, 10)
            y = random.randint(0,10)
            res = x * y

            print(f"Quanto fa {x} x {y} ?")
            risposta = int(input("Inserisci risultato:"))

            if risposta == res:
                count += 1
        print(f"Hai risolto {count} su 5.")

    elif comando == 3:
        x = random.randint(1, 30)
        print("Il numero segreto è multiplo di:")

        for i in range(1, x):
            if x % i == 0:
                print(i)
        
        risposta = int(input("Inserire numero: "))

        if risposta == x:
            print("Hai indovinato!")
        else:
            print("Hai perso. Il numero era:", x)

    else:
        print("Comando non valido.")


    print()
    print("1) Indovina x")
    print("2) Gara tabelline")
    print("3) Indovina x difficile")
    comando = int(input("Inserire comando: "))

print("A PRESTO")