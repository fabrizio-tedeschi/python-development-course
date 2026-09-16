#Definizione di una funzione
def foo(a, b, c):
    out = (a * b) + c
    return out

#Chiamata della funzione cond diversi valori e stampa del risultato
print("foo(1, 2, 3) ha restituito", foo(1, 2, 3))
print("foo(0, 2, 3) ha restituito", foo(0, 2, 3))
print("foo(5, 10, 15) ha restituito", foo(5, 10, 15))
print("foo(1, \"aaaaaa\", 3) ha restituito", foo(1, "aaaaaaa", 3)) #Errore