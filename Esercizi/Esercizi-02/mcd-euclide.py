a = int(input("Inserisci a: "))
b = int(input("Inserisci b: "))

while a<=0:
    print("Il numero a deve essere maggiore di 0")
    a = int(input("Inserisci a: "))

while b<=0:
    print("Il numero b deve essere maggiore di 0")
    b = int(input("Inserisci b: "))

if a < b:
    tmp = a
    a = b
    b = tmp

r = a % b
while r != 0:
    a = b
    b = r
    r = a % b

print("Il Massimo Comune Divisore (MCD) è:", b)