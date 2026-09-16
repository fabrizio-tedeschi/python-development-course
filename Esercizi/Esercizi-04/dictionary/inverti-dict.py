#Inizializzazione dictionary
d = {
    "a": 10,
    "b": 20,
    "c": 15,
}

d1 = {}

for k, v in d.items():
    d1[v] = k

print(d1)