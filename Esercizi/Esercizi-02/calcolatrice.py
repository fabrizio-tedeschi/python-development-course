print("CALCOLATRICE PYTHON")
comando = input("Inserire operazione: ")

while comando != "#":

    a = int(input("Inserire primo numero: "))
    b = int(input("Inserire secondo numero: "))
    res = ""

    match comando:
        case "+":
            res = a + b
        case "-":
            res = a - b
        case "*":
            res = a * b
        case "/":
            if b == 0:
                print("Non puoi dividere per zero!")
            else:
                res = a / b
        case _:
            print("Operatore non valido!")
    
    if res != "":
        print("Risultato:", res)

    print()
    comando = input("Inserire operazione: ")

print("A PRESTO!")