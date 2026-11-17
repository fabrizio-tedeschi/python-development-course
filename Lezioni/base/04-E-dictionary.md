# Dictionary

I **dictionary** sono insiemi di coppie chiave-valore in cui ciascuna chiave è associata al corrispondente valore.

* Ciascuna *chiave* è un elemento immutabile (stringa o intero che sia)
* Ciacun *valore* è un elemento che può essere un numero, una stringa, una lista, una tupla o un'altro dictionary

## Operazioni elementari

Un dizionario può essere creato o inizializzato come mostrato di seguito grazie all'utilzzo delle `{}`:

```python
# Creazione di un dictionary vuoto
empty_dict = {}

# Inizializzazione di un dictionary con chiavi e valori
frutta = {
    "mele": 15,
    "pere": 20,
    "ananas": 10
}
```

### Accesso e modifica di elementi

Per accedere/modificare elementi di un dizionario è possibile utilizzare l'operatore `[]` posto al termine del nome del dizionario.

```python
# Accesso al valore data una chiave
x = frutta["mele"]
print(x)                # Stampa: 15

# Modifica di un valore data una chiave
frutta["mele"] = 5
print(frutta)           # Stampa: {'mele': 5, 'pere': 20, 'ananas': 10}
```

**NB**: se si prova a estrarre un valore fornendo una chiave inesistente viene generato un `KeyError` che interrompe il programma.

### Aggiunta ed eliminazione di chiavi

Si possono aggiungere o eliminare coppie chiave-valore come mostrato di seguito:

```python
# Aggiunta di una coppia chiave-valore
frutta["kiwi"] = 3
print(frutta)           # Stampa: {'mele': 5, 'pere': 20, 'ananas': 10, 'kiwi': 3}

# Eliminazione di una coppia chiave-valore
del frutta["ananas"]
print(frutta)           # Stampa: {'mele': 5, 'pere': 20, 'kiwi': 3}
```

**NB**: se si prova a eliminare un valore fornendo una chiave inesistente viene generato un `KeyError` che interrompe il programma.

### Controlli sulla presenza di chiavi

L'operatore `in` permette di verificare se una chiave è presente all'interno di un dizionario.

```python
p = "mele" in frutta
print(p)                # Stampa: True

p = "fragole" in frutta
print(p)                # Stampa: False
```

## Metodi dei dictionary

I **metodi** sono funzioni proprie dei dizionari. Essi si applicano alla variabile che identifica il dizionario tramite l'operatore punto: `.nome_metodo()`

* `.keys(i, e)`: restituisce un oggetto vista `dict_keys` con tutte **le chiavi** del dizionario;
* `.values(i, e)`: restituisce un oggetto vista `dict_values` con **i valori** del dizionario;
* `.items(i, e)`: restituisce un oggetto vista `dict_items` contenente tuple formate da `(chiave, valore)`;

* `.get(k, default)`: ritorna il valore corrispondente alla chiave `k` passata se questa esiste. Se la chiave non esiste ritorna `None` oppure il valore `default` se impostato;
* `.update(other)`: unisce i valori del dizionario `other` a quelli del dizionario corrente aggiungendo le nuove chiavi e sovrascrivendo quelle già esistenti;
* `.pop(k, default)`: rimuove la chiave specificata e ne restituisce il valore. Se la chiave non esiste ed è impostato un valore `default` allora viene restituito quel valore altrimenti viene sollevato un `KeyError`;

```python
d1 = {
    "mele": 15,
    "pere": 20,
}

d2 = {
    "ananas": 5,
    "pere": 10,
}

# Aggiorno d1 con d2
d1.update(d2)
print(d1)                   # Stampa: {'mele': 15, 'pere': 10, 'ananas': 5}

# Rimuovo una chiave da d2
popped = d2.pop("pere", 0)
print(popped)               # Stampa: 10
print(d2)                   # Stampa: {'ananas': 5}
```

### Iterazione su dictionary

Per iterare sugli oggetti di un dictionary è possibile utilizzare una coppia di variabili come mostrato nel seguito:

```python
# Iterazione su oggetti di un dictionary
for k, v in my_dict.items():
    # Operazioni da svolgere durante ciascuna iterazione

# Operazioni successive
```
