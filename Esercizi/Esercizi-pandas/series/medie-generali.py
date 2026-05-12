import pandas as pd

medie = {
    "Rossi": 7.96,
    "Verdi": 8.32,
    "Bianchi": 5.90,
    "Neri": 9.21,
    "Bossi": 9.21,
    "Santi": 5.32
}

s = pd.Series(medie)
print(s)

print("\nStudenti con media sufficiente:")
print(s[s >= 6.0])

print("\nStudenti con media insufficiente:")
print(s[s < 6.0])

best = s[s == s.max()].index[0]
print("\nStudente con media migliore:", best)

worst = s[s == s.min()].index[0]
print("Studente con media peggiore:", worst)