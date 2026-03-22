from math import sqrt

#Definizione della funzione
def risolvi_equazione(a, b, c):
    print()
    print("-> Soluzioni di", a, "x^2", b, "x", c, "= 0")
    print()

    if a == 0:
        print("Non equazione di secondo grado: a = 0")
    else:
        delta = b*b - 4*a*c

        if delta < 0:
            print("L'equazione non possiede soluzioni reali!")
        else:
            x1 = (-b + sqrt(delta))/(2*a)
            x2 = (-b - sqrt(delta))/(2*a)

            print("x1 =", x1)
            print("x2 =", x2)


#Istruzioni di test
risolvi_equazione(0, 0, 0)
risolvi_equazione(1, 0, 0)
risolvi_equazione(-0.5, 2, -1)
risolvi_equazione(4, 1, 2)
