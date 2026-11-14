x = int(input("Inserisci x: "))
y = int(input("Inserisci x: "))
punto = (x, y)

dx = int(input("Inserisci spostamento x: "))
dy = int(input("Inserisci spostamento y: "))
spostamento = (dx, dy)

nuovo = (punto[0]+spostamento[0], punto[1]+spostamento[1])
print("Punto spostato:", nuovo)