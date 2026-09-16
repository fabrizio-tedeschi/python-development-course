def is_prime(n):
    if x <= 0:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

test = [1, 13, 10, 100, 101]
for x in test:
    print(f"Verifico se {x} è primo: ")
    print(is_prime(x))