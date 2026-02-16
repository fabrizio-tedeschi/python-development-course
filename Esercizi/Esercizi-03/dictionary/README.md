# Esercizi 03 - Dictionary

### (A) - prodotti.py

Inizializzare un dictionary vuoto `prodotti`. Ciascuna chiave di tale dictionary è costituita da un intero progressivo maggiore di 1,
ciascun valore da una stringa che contiene il nome di un prodotto di un supermercato.

Si chieda all'utente di inserire 10 prodotti e successivamente si stampi ciascun prodotto (valore) assieme al proprio codice associato (chiave).

### (B) - estrazione-chiavi.py

Dato il seguente dictionary:

```python
dict = {
    "k1": "Primo elemento",
    "Chiave-2": False,
    3: 157,
    7: [0, 0, 0] 
}
```

Stampare ciascuna delle sue chiavi.

### (C) - inverti-dict.py

Dato un dictionary `d` creare e stampare un nuovo dictionary `d1` che abbia chiavi e valori invertiti rispetto a quello di origine. Per esempio:

```python

# Partendo da
d = {
    "a": 10,
    "b": 20,
    "c": 15,
}

# Si ottiene
d1 = {
    10: "a",
    20: "b",
    15: "c",
}
```

### (D) - nuotatori.py

Chiedere in input un numero `k` all'utente e avviare una procedura che richiede l'inserimento dei dati di `k` nuotatori.

Ogni blocco di dati possiede i seguenti quattro attributi: nome, cognome, stile, tempo (misurato in secondi).

Dopo l'inserimento dei dati il programma esegue le seguenti operazioni:
* Stampa l'elenco dei nomi e dei cognomi dei nuotatori
* Stampa i cognomi dei nuotatori che hanno nuotato a stile `Free` in un tempo inferiore a 98 secondi.
* Stampa tutti i dati del nuotatore che ha effettuato il tempo più basso.

Testare il programma inserendo i seguenti dati:

| Nome | Cognome | Stile | Tempo |
|------|---------|-------|-------|
|Mario|Rossi|Rana|125|
|Luigi|Verdi|Free|95|
|Anna|Bianchi|Free|80|
|Giulia|Monti|Free|100|

### (E) - classifica-nuotatori.py

Inizializzare una lista `nuotatori` con 4 dictionary contenenti i dati mostrati nella tabella dell'esercizio precedente.

Stampare la classifica dei nuotatori posizionando coloro che hanno effettuato il miglior tempo in alto.

La classifica deve avere il seguente formato di stampa:
 ```
 1. Bianchi - 80 - Free
 2. Verdi - 95 - Free
 ```

Stampare in modo analogo la classifica dei soli nuotatori con stile `Free`.

>**Suggerimento**: per prima cosa è necessario riordinare la lista per miglior tempo. Successivamente la si scorre tutta e si procede alla stampa con le posizioni in classifica.

### (F) - conta-protti.py

Un utente inserisce in un programma un numero `n` di prodotti che desidera inserire in un carrello e succesisvamente inserisce gli `n` prodotti uno per volta. L'utente può acquistare più pezzi dello stesso prodotto inserendolo tante volte quanti sono i pezzi che desidera acquistare.

*Esempio*: se l'utente inserisce la sequenza `mela`, `pera`, `banana`, `mela` significa che desidera acquistare 2 mele, 1 pera e 1 banana.

Si scriva un programma che chieda all'utente un numero `n` e successivamente l'inserimento di `n` prodotti uno per volta. Terminato l'inserimento dei prodotti il programma stampa un dictionary che ha per chiavi i nomi di ciascun prodotto inserito e per valori il numero di pezzi di ciascun prodotto che l'utente desidara acquistare.

Inserendo i dati dell'esempio precedente si ottiene:

```python
{
    "mela": 2,
    "pera": 1,
    "banana": 1
}
```

### (G) - magazzino.py

Si considerino i seguenti dictionary che rappresentano i prodotti all'interno di due magazzini `m1` e `m2`:

```python
m1 = {"computer": 20, "frigoriferi": 6, "smartphone": 50}
m2 = {"computer": 25, "smartphone": 30, "lavatrici": 5, "lavastoviglie": 8}
```

Si scriva un programma che crei un dictionary che contenga tutti i diversi prodotti presenti nei vari magazzini e il loro numero complessivo. Nel caso considerato si otterrebbe:

```python
{
    "computer": 45,
    "frigoriferi": 6,
    "smartphone": 80,
    "lavatrici": 5,
    "lavastoviglie": 8
}
```

## (H) - ordini.py

Data la seguente lista di ordini:

```python
ordini = [
    {"id": 1, "cliente": "Marco", "spesa": 250, "pagato": True},
    {"id": 2, "cliente": "Anna", "spesa": 120, "pagato": False},
    {"id": 3, "cliente": "Marco", "spesa": 75, "pagato": True},
    {"id": 4, "cliente": "Luca", "spesa": 310, "pagato": False},
    {"id": 5, "cliente": "Anna", "spesa": 90, "pagato": True}
]
```

Scrivere un programma che:
1. Calcola e stampa il totale delle spese
2. Crea un dictionary `spese` con i nomi di ogni cliente come chiavi e il totale della spesa per ciascun cliente come valori
3. Crea una nuova lista `nonpagati` e ci inserisce solamente i dictionary degli ordini non pagati (ossia gli ordini che hanno `"pagato"==False`)

Per il punto 2 si vuole ottenere un dictioanry come quello che segue:

```python
{
    "Marco": 325,
    "Anna": 210,
    "Luca": 310
}
```

Per il punto 3 si vuole ottenere una lista come quella che segue:

```python
nonpagati = [
    {"id": 2, "cliente": "Anna", "spesa": 120, "pagato": False},
    {"id": 4, "cliente": "Luca", "spesa": 310, "pagato": False},
]
```