#Definizione della funzione
def dati_maggiorenni(lista):
    maggiorenni = []

    for persona in lista:
        if persona.get("Anni") >= 18:
            maggiorenni.append(persona)

    return maggiorenni

#Istruzioni di test
persone = [
    {"Nome": "Mario", "Cognome": "Rossi", "Anni": 15, "Altezza": 175},
    {"Nome": "Luigi", "Cognome": "Verdi", "Anni": 23, "Altezza": 168},
    {"Nome": "Anna", "Cognome": "Bianchi", "Anni": 56, "Altezza": 181},
    {"Nome": "Luisa", "Cognome": "Rinaldi", "Anni": 16, "Altezza": 157},
    {"Nome": "Stefano", "Cognome": "Baruzzi", "Anni": 12, "Altezza": 178},
    {"Nome": "Maria", "Cognome": "Callas", "Anni": 35, "Altezza": 190}
]

print("Elenco delle persone maggiorenni:")
for maggiorenne in dati_maggiorenni(persone):
    print("-->", maggiorenne)