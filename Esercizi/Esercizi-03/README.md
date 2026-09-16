# Esercizi 04 - Funzioni

> Svolgere i seguenti esercizi definendo le funzioni richieste e svolgendo opportuni test di funzionamento.

### area-triangolo.py

Definire una funzione `area_triangolo(base, altezza)`. La funzione accetta base e altezza (in centimetri) di un triangolo e restituisce la sua area.

### somma-numeri.py

Scrivere una funzione `somma_numeri` che accetta un numero `n` e ritorna la somma di tutti i numeri interi da `1` fino a `n`.

Testare la funzione chiedendo in input il valore `n` all'utente, passarlo alla funzione e stampare il risultato.

### perfetto.py

Un numero è **perfetto** se è uguale alla somma dei suoi divisori escluso il numero stesso. Creare una funzione `is_perfect()` che dato un numero `x` ritorna `True` se il numero è perfetto, `False` altrimenti.

Si verifichino anche i casi particolari `x = 0` e `x = 1`.

### serie-geometrica.py

Un valore n-esimo della **serie geometrica** viene definito come `S(n) = 1 + q + q^2 + q^3 + ... + q^n`. Definire una funzione `serie_geometrica` che accetta i valori `n` e `q` e che calcola e restituisce il valore `S(n)`.

Chiedere i valori `n` e `q` in input all'utente forzando l'inserimento di valori positivi.

### potenza.py

Definire una funzione `potenza(base, esponente)`. La funzione calcola la potenza con base `base` ed esponente `esponente`
restituendo il risultato. La funzione deve effettuare tutti i controlli necessari su base ed esponente (es. numeri negativi).
Per lo svolgimento di questo esercizio viene fatto divieto dell'utilizzo dell'operatore `**`.

### fattoriale.py

In matematica il **fattoriale** di un numero `n` viene definito come `n! = n * (n-1) * (n-2) ...`. Il fattoriale di 5 per esempio sarà `5! = 5 * 4 * 3 * 2 * 1`. Inoltre per definizione `0! = 1`.

Definire una funzione `fattoriale(n)` che accetta un numero intero positivo `n` e ne calcola il fattoriale restituendolo
come valore di ritorno.

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

![formula](../../Lezioni/base/images/formula-equazioni.jpg)

**IMPORTANTE**: se DELTA risulta essere minore di 0, l'equazione NON possiede soluzioni reali.

Definire una funzione `risolvi_equazione(a, b, c)` che accetta i parametri di una equazione di secondo grado e stampa su `output` le due possibili soluzioni.
Effettuare tutti i controlli opportuni sui parametri forniti e sul valore di delta calcolato.

### primo.py

Per definizione un numero `n` è **primo** se è divisibile solo per 1 e per sè stesso. Per verificare se un numero non è primo è sufficiente trovare un altro suo divisore oltre a 1 e a `n`.

Definire una funzione `is_prime(n)` che dato un numero `n` restituisce `True` se il numero è primo altrimenti restituisce `False`. Se il numero è negativo o nullo la funzione restituisce `False`.