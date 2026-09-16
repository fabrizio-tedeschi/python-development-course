def crivello(k):
    out = []

    for i in range(2, k+1):
        multiplo = False
        
        for num in out:
            if i % num == 0:
                multiplo = True
                break
        
        if multiplo == False:
            out.append(i)

    return out

x = int(input("Inserisci numero: "))
l = crivello(x)

print()
print(f"Numeri primi fra 2 e {x}:")
print(l)