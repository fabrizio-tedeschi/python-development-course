magazzino = [("viti", 120, 0.05), ("bulloni", 4, 0.20),
             ("chiodi", 300, 0.02), ("rondelle", 3, 0.10)
]

valore_totale = 0
for p in magazzino:
    valore_totale += p[1]*p[2]
print("Valore totale magazzino:", round(valore_totale,2))

print("Prodotti sottoscorta:")
for p in magazzino:
    if p[1] < 5:
        print("-", p[0])