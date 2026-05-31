n = int(input("Inserire numero: "))
seq = ""

while n >= 0:
    seq += str(n)
    n = int(input("Inserire numero: "))

print(seq)