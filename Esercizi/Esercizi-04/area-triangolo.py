#Definizione della funzione
def area_triangolo(base, altezza):
    area = base * altezza / 2
    return area

#Istruzioni di test
print(area_triangolo(5, 10))
print(area_triangolo(2, 5))
print(area_triangolo(0, 3))
print(area_triangolo(7, 0))