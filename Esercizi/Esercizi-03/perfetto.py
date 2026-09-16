def is_perfect(x):
    if x == 0 or x == 1:
        return False
    
    somma = 0
    for i in range(1, x):
        # Se i è divisore di x
        if x%i == 0:
            somma += i

    if somma == x:
        return True
    else:
        return False

test = [0, 1, 6, 7]
for n in test:
    print(f"Verifico se {n} è perfetto:")
    print(is_perfect(n))