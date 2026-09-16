n = int(input("Inserire un numero: "))
s = str(n)

out = ""
for cifra in s:
    if int(cifra) % 2 == 0:
        out = out + cifra + "-"

out = out[:-1]
print(out)