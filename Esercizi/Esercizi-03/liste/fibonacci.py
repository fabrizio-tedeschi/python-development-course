n = int(input("Inserire numero: "))
while n < 0:
    print("Il numero deve essere positivo!")
    n = int(input("Inserire numero: "))

successione = []

for i in range(n):
    if i == 0:
        successione.append(0)
    elif i == 1:
        successione.append(1)
    else:
        num = successione[i-1] + successione[i-2]
        successione.append(num)

print(successione)