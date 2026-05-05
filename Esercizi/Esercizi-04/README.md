# Esercizi 04 - Funzioni

> Svolgere i seguenti esercizi definendo le funzioni richieste e svolgendo opportuni test di funzionamento.

### area-triangolo.py

Definire una funzione `area_triangolo(base, altezza)`. La funzione accetta base e altezza (in centimetri) di un triangolo e restituisce la sua area.

### somma-numeri.py

Scrivere una funzione `sommanumeri` che accetta un numero `n` e ritorna la somma di tutti i numeri interi da `1` fino a `n`.

Testare la funzione chiedendo in input il valore `n` all'utente, passarlo alla funzione e stampare il risultato.

### fattoriale.py

In matematica il fattoriale di un numero `n` viene definito come `n! = n * (n-1) * (n-2) ...`. Il fattoriale di 5 per
esempio sarà `5! = 5 * 4 * 3 * 2 * 1`. Inoltre per definizione `0! = 1`.

Definire una funzione `fattoriale(n)` che accetta un numero intero positivo `n` e ne calcola il fattoriale restituendolo
come valore di ritorno.

### potenza.py

Definire una funzione `potenza(base, esponente)`. La funzione calcola la potenza con base `base` ed esponente `esponente`
restituendo il risultato. La funzione deve effettuare tutti i controlli necessari su base ed esponente (es. numeri negativi).
Per lo svolgimento di questo esercizio viene fatto divieto dell'utilizzo dell'operatore `**`.

### fizzbuzz.py

Definire una funzione `fizzbuzz` che accetta un numero `n` e stampa i valori da `1` fino a `n` ma che rimpiazza alcuni valori della sequenza come segue:
* Al posto di ciascun numero multiplo di 3 stampa `fizz`
* Al posto di ciascun numero multiplo di 5 stampa `buzz`
* Al posto di ciascun numero multiplo sia di 3 sia di 5 stampa `fizzbuzz`

Per esempio chiamando la funzione `fizzbuzz(15)` essa produrrà la sequenza:

```
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
```

Ma stamperà:

```
1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz
```

### equazioni.py

In matematica le soluzioni di una quazione di secondo grado del tipo `ax^2 + bx + c = 0`si calcolano tramite la seguente formula:

![formula](../../Lezioni/images/formula-equazioni.jpg)

**IMPORTANTE**: se DELTA risulta essere minore di 0, l'equazione NON possiede soluzioni reali.

Definire una funzione `risolvi_equazione(a, b, c)` che accetta i parametri di una equazione di secondo grado e stampa su `output` le due possibili soluzioni.
Effettuare tutti i controlli opportuni sui parametri forniti e sul valore di delta calcolato.

## Funzioni e liste

### somma-multipli.py

Definire e testare una funzione che data una lista `l` di numeri interi e un numero `n`, ritorna la somma dei soli multipli di `n`.

### filtra-nomi.py

Definire una funzione che data una lista `l` di nomi (stringhe) e un carattere `ch` ritorna una nuova lista contenente solo i nomi che iniziano con la lettera `ch`.

### filtra-parole.py

Definire una funzione che data una lista `l` di parole (stringhe) e una stringa `s` ritorna una nuova lista contenente solo le parole che iniziano con la stringa `s`.

### rimuovi-occorrenze.py

Definire una funzione `rimuovi_occorrenze(l, e)` che accetta una lista `l` e un elemento `e`. La funzione restituisce una nuova
lista dalla quale sono state rimosse tutte le occorrenze di `e`.

### dati-maggiorenni.py

Definire una funzione `dati_maggiorenni(lista)`. La funzione accetta una lista di dictionary contenenti i dati di alcune persone.
Il compito della funzione è quello di restituire una nuova lista che contenga solamente i dati delle persone maggiorenni.

Si utilizzi la lista di persone fornita di seguito per effettuare i test necessari.

```python
persone = [
    {"Nome": "Mario", "Cognome": "Rossi", "Anni": 15, "Altezza": 175},
    {"Nome": "Luigi", "Cognome": "Verdi", "Anni": 23, "Altezza": 168},
    {"Nome": "Anna", "Cognome": "Bianchi", "Anni": 56, "Altezza": 181},
    {"Nome": "Luisa", "Cognome": "Rinaldi", "Anni": 16, "Altezza": 157},
    {"Nome": "Stefano", "Cognome": "Baruzzi", "Anni": 12, "Altezza": 178},
    {"Nome": "Maria", "Cognome": "Callas", "Anni": 35, "Altezza": 190}        
]
```
