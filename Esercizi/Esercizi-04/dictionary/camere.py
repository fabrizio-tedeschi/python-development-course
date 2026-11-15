s = int(input("Camere singole: "))
d = int(input("Camere doppie: "))
sup = int(input("Camere superior: "))

camere = {
    "singole": s,
    "doppie": d,
    "superior": sup
}

print("Camere con meno di 50 vendite:")
for k, v in camere.items():
    if v < 50:
        print("-", k)

camera_max=""
val_max = 0
for k, v in camere.items():
    if v > val_max:
        val_max = v
        camera_max = k
print("Camera più venduta:", camera_max)
# Oppure: camera_max = max(camere, key=camere.get)

totale_vendite = 0
for v in camere.values():
    totale_vendite += v
print("Totale camere vendute:", totale_vendite)
# Oppure: totale_vendite = sum(list(camere.values))

guadagno = 0
guadagno += camere["singole"] * 45
guadagno += camere["doppie"] * 90
guadagno += camere["superior"] * 110
print("Guadagno stagione:", guadagno)