def somma_multipli(l, n):
    somma = 0
    for num in l:
        if num % n == 0:
            somma += num
    
    return somma


l = [5, 6, 7, 10, 12, 15, 20, 30]

r = somma_multipli(l, 5)
print("Somma multipli di 5:", r)

r = somma_multipli(l, 10)
print("Somma multipli di 10:", r)