n = int(input("Inserire numero: "))
while n < 0:
    print("Il numero deve essere positivo!")
    n = int(input("Inserire numero: "))

successione = []

for i in range(n):
    if i < 3:
        num = 1
    else:
        num = successione[i-2] + successione[i-3]
    successione.append(num)

print(successione)