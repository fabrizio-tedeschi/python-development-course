#Inizializzione di un dictionary vuoto
my_dict = {}

#Aggiunta di elementi
my_dict["Chiave-1"] = 133
my_dict["Chiave-2"] = 100
my_dict["Terza"] = 75.32
my_dict[4] = True

#Stampa delle sole chiavi
print("Elenco delle chiavi:", my_dict.keys())
print()

#Stampa dei soli valori
print("Elenco dei valori:", my_dict.values())
print()

#Scorrimento delle coppie chiave-valore
for key, value in my_dict.items():
    print(key, value)
print()

#Accesso con chiave inesistente
print("Provo ad accedere all'elemento con chiave k4 (inesistente)...")
print(my_dict.get("k4"))
print(my_dict.get("k4", "MY_ERROR: Chiave inesistente!"))

print(my_dict["k4"]) #Genera ERRORE