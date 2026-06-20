def isprime(n):
    if x <= 0:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

x = 1
print(f"Verifico se {x} è primo: ")
print(isprime(x))

x = 13
print(f"Verifico se {x} è primo: ")
print(isprime(x))

x = 10
print(f"Verifico se {x} è primo: ")
print(isprime(x))

x = 100
print(f"Verifico se {x} è primo: ")
print(isprime(x))

x = 101
print(f"Verifico se {x} è primo: ")
print(isprime(x))