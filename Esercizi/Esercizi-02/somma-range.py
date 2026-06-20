a = int(input("Inserisci a: "))
b = int(input("Inserisci b: "))

while a >= b:
    print("Errore: a deve essere minore di b!")
    a = int(input("Inserisci a: "))
    b = int(input("Inserisci b: "))

somma = 0
for i in range(a, b+1):
    somma += i

print(f"Somma dei valori fra {a} e {b}:", somma)