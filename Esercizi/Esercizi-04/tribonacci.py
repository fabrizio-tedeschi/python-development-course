def tribonacci(n):
    out = []

    for i in range(n):
        if i <= 1:
            x = 0
        elif i == 2:
            x = 1
        else:
            x = out[i-1] + out[i-2] + out[i-3]
        out.append(x)

    return out

successione = tribonacci(-1)
print(successione)

successione = tribonacci(2)
print(successione)

successione = tribonacci(8)
print(successione)