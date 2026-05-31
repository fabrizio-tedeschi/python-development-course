# Esercizi 02 - Strutture di selezione e ripetizione

## Strutture di selezione if/elif/else

### segno.py

Scrivere un programma che chiede in input all'utente un numero e verifica se tale numero è positivo, negativo oppure zero. Il programma stampa un opportuno messaggio su terminale.

### maggiorenne.py

Scrivere un programma che accetta in input nome, cognome e anni di una persona. Il programma stampa su output i dati della persona e se è maggiorenne o meno.

### abbonamento-palestra.py

Scrivere un programma che si occupa di calcolare il costo di un abbonamento di una palestra seguendo i seguenti criteri:

* Ogni abbonamento ha un costo mensile di 30€
* Se l'utente è minorenne si ha una aggiunta di 10€ per l'assicurazione
* Le persone con età inferiore a 20 anni o superiore a 60 hanno uno sconto del 20% sul prezzo complessivo
* Se l'abbonamento supera i 4 mesi si ha diritto a uno sconto del 30% sul totale, se supera gli 8 mesi si ha diritto a uno sconto del 40% sul totale.
* Gli sconti dovuti all'età e al numero di mesi sono cumulabili.

Chiedere in input all'utente l'età e il numero di mesi per i quali desidera effettuare l'abbonamento e stampare il costo dell'abbonamento.

## Ciclo while

### somma-prodotto.py

Scrivere un programma che accetta in input dall'utente una serie di numeri interi (uno alla volta) fino a quando l'utente inserisce il valore 0. Prima di terminare il programma stampa su output la **somma** ed il **prodotto** di tutti i numeri passati dall'utente.

### media.py

Scrivere un programma che accetta in input dall'utente una serie di numeri interi fino a quando l'utente inserisce il valore 0. Prima di terminare il programma stampa su output la MEDIA di tutti i numeri passati dall'utente (escluso lo 0).

### max-serie.py

Scrivere un programma che accetta in input una serie di numeri interi positivi fino a quando viene inserito il valore 0. Il programma, prima di terminare, stampa su output il valore massimo inserito.

### min-serie.py

Scrivere un programma che accetta in input una serie di numeri interi sia positivi che negativi fino a quando viene inserito il valore 0. Il programma, prima di terminare, stampa su output il valore massimo inserito.

### pari-dispari.py

Scrivere un programma che accetta in input dall'utente una serie di numeri interi fino a quando l'utente inserisce il valore 0. Per ciascun numero, dopo l'inserimento, stampare se è pari o dispari.

### multipli.py

Scirvere un programma che chiede in input all'utente un numero `x` positivo strettamente maggiore di zero (forzare l'inserimento in caso di valori errati).

Il programma chiede poi all'utente una sequenza di numeri (uno per volta) fino a quando l'utente inserisce il valore 0.

Il programma stampa quanti fra i valori inseriti dall'utente sono multipli di `x`.

### sequenza.py

Scrivere un programma che chiede all'utente una serie di numeri interi (>= 0). Per terminare il programma l'utente può inserire un qualsiasi numero negativo.
Il programma deve stampare la sequenza dei numeri inseriti dall'utente sotto-forma di stringa.
Per esempio se l'utente inserisce 1, 5, 8, 22, 6, -5 allora il programma stamperà "158226".

### indovina-numero.py

Scrivere un programma che calcola randomicamente un numero `x` comrpeso fra 0 e 20. Successivamente, il programma valuta una serie di valori inseriti dall'utente e stampa il messaggio *troppo alto* o *troppo basso* per aiutare l'utente a indovinare il numero. Il programma si ferma quando l'utente indovina il numero `x`.

### cassa.py

Scrivere un programma che simula una cassa: accetta in input i prezzi dei prodotti (uno alla volta, come numeri decimali) fino a quando l'utente inserisce 0. Il programma stampa il totale, chiede quanto ha pagato il cliente e stampa il resto. Se il cliente paga meno del totale, segnalarlo e chiedere di reinserire l'importo.

### offerte.py

Scrivere un programma che simula un confronto prezzi: accetta in input i prezzi di uno stesso prodotto rilevati in negozi diversi (uno alla volta, come numeri decimali positivi) fino a quando l'utente inserisce 0. Il programma stampa il prezzo più alto trovato e quanti negozi applicavano esattamente quel prezzo massimo. Se non viene inserito nessun prezzo, stampare un messaggio appropriato.

### mcd-euclide.py

L'algoritmo di euclide permette di calcolare il MCD fra due numeri `a` e `b` (con `a < b`) come descritto di seguito.

Forzare l'inserimento di entrambi `a` e `b` maggiori di 0.

* Il programma chiede in input all'utente i numeri `a` e `b`.
* Se per caso `a > b` allora `a` e `b` vengono scambiati.
* Il programma calcola il resto `r` della divisione fra `a` e `b`
    * Se `r = 0` allora `b` è il MCD
    * Se `r != 0` allora `a` assume il valore di `b` e `b` assume il valore `r` e si ripetono le operazioni precedenti.