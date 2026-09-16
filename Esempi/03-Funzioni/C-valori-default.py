#Definizione di una funzione con valori di default
def stampa_parole(s1, s2, s3 = "."):
    out = s1 + s2 + s3
    print(out)

#Invocazioni della funzione
stampa_parole("alfa", "beta")
stampa_parole("alfa", "beta", "gamma")
stampa_parole("alfa", "beta", "!")