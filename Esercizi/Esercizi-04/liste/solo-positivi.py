def solo_positivi(l):
    out = []
    for num in l:
        if num > 0:
            out.append(num)
    return out

l = [3, -1, 0, 8, -5]
out = solo_positivi(l)
print(f"Lista: {l}. \tOut: {out}")

l = [-3, -1, 0, -8, -5]
out = solo_positivi(l)
print(f"Lista: {l}. \tOut: {out}")

l = []
out = solo_positivi(l)
print(f"Lista: {l}. \t\t\tOut: {out}")