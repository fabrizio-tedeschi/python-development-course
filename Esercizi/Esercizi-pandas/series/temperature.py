import pandas as pd

days = ["lun", "mar", "mer", "gio", "ven", "sab", "dom"]
temps = []

for d in days:
    t = float(input("{}: inserisci temperatura: ".format(d)))
    temps.append(t)

s = pd.Series(temps, days)
print(s)

over = s[s >= 25.0].count()
under = s[s <= 5.0].count()

mask = (s > 5.0) & (s < 25.0)
between = s[mask].count()

print()
print("Temps over 25.0°C:", over)
print("Temps under 5.0°C:", under)
print("Temps between:", between)