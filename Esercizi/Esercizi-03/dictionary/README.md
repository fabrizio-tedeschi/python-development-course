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

### (C) - estrazione-coppie.py

Dato il seguente dictionary:

```python
mydict = {
    "k1": "Primo elemento",
    "Chiave-2": False,
    3: 157,
    7: [0, 0, 0] 
}
```

Stampare su `stdout` ciascuna coppia chiave-valore come mostrato di seguito:

```
Elemento Primo elemento con chiave k1
Elemento False con chiave Chiave-2
Elemento 157 con chiave 3
Elemento [0, 0, 0] con chiave 7
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