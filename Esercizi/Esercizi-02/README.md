# Esercizi 02 - Strutture di selezione e ripetizione

## Strutture di selezione

### maggiorenne.py

Scrivere un programma che accetta in input nome, cognome e anni di una persona. Il programma stampa su output i dati della persona e se è maggiorenne o meno.

### calcola-anni.py

Scrivere un programma che chiede in input all'utente l'anno in cui è nato e un anno futuro. Il programma calcola e stampa quanti anni avrà l'utente nell'anno inserito.

Se l'anno inserito dall'utente è precedente all'anno di nascita allora il programma stampa un messaggio di errore dato che una persona non può avere un numero negativo di anni.

### segno.py

Scrivere un programma che chiede in input all'utente un numero e verifica se tale numero è positivo, negativo oppure zero. Il programma stampa un opportuno messaggio su terminale.

### abbonamento-palestra.py

Scrivere un programma che si occupa di calcolare il costo di un abbonamento di una palestra seguendo i seguenti criteri:

* Ogni abbonamento ha un costo mensile di 30€
* Se l'utente è minorenne si ha una aggiunta di 10€ per l'assicurazione
* Le persone con età inferiore a 20 anni o superiore a 60 hanno uno sconto del 20% sul prezzo complessivo
* Se l'abbonamento supera i 4 mesi si ha diritto a uno sconto del 30% sul totale, se supera gli 8 mesi si ha diritto a uno sconto del 40% sul totale.
* Gli sconti dovuti all'età e al numero di mesi sono cumulabili.

Ogni volta che il programma applica uno sconto o un supplemento stampa un opportuno messaggio.

Chiedere in input all'utente l'età e il numero di mesi per i quali desidera effettuare l'abbonamento e stampare il costo dell'abbonamento.

### noleggio-bici.py

Scrivere un programma che calcola il costo del noleggio di una bicicletta in base ai seguenti criteri:

* Il noleggio ha un costo base di 5€ all'ora
* Per ogni ora di noleggio viene aggiunto un supplemento di 2,5€
* Se la bici è elettrica (l'utente risponde si/no), si aggiunge un supplemento fisso di 8€
* Gli studenti (l'utente risponde si/no) hanno uno sconto del 15% sul prezzo complessivo
* Se il noleggio supera le 3 ore si ha diritto a uno sconto del 10% sul totale, se supera le 6 ore lo sconto sale al 25%
* Gli sconti per studenti e per durata sono cumulabili

Ogni volta che il programma applica uno sconto o un supplemento stampa un opportuno messaggio.

Chiedere in input all'utente: se la bici è elettrica, se chi la noleggia è studente e il numero di ore di noleggio, quindi stampare il costo finale.

### mensa.py

Scrivere un programma che simula l'ordinazione di piatti in una mensa, utilizzando il costrutto `match case` per gestire la scelta del piatto.

L'utente indica in input:
* Il numero del piatto che desidera ordinare
* La quantità di pezzi
* Se desidera il servizio al tavolo

Il menu a disposizione è il seguente:

  | Numero | Piatto              | Prezzo |
  |--------|---------------------|--------|
  | 1      | Pizza margherita    | 6€     |
  | 2      | Pasta al pomodoro   | 7€     |
  | 3      | Insalata mista      | 5€     |
  | 4      | Hamburger           | 9€     |
  | 5      | Tiramisù            | 4€     |

Se l'utente inserisce un numero non presente nel menu (diverso da 1-5), il programma deve stampare il messaggio di errore *Piatto non disponibile: ordinerai una pizza* e applicare il costo della pizza.

Per calcolare il costo dell'ordine:
1. Si moltiplica il costo del piatto per il numero di pezzi
2. Se l'utente ha scelto il servizio al tavolo si aggiunge un supplemento di 2€ a persona dopo aver chiesto il numero di persone all'utente.
3. Se la quantità totale di piatti ordinati supera le 4 unità si ha diritto a uno sconto del 10% sul totale; se supera le 8 unità lo sconto sale al 20%.

Stampare il totale dell'ordine.

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

## Ciclo for

### divisori.py

Chiedere in input all'utente un numero `n` forzando l'inserimento di un numero non negativo e stampare tutti i suoi divisori. Per definizione un numero `d` è divisore di `n` se `n/d` fornisce resto zero.

### tabellina.py

Chiedere in input all'utente un numero `n` forzando l'inserimento di un numero non negativo e stampare la sua tabellina. Per esempio:

```
3 x 0 = 0
3 x 1 = 3
...
3 x 10 = 30
```

### somma-range.py

Scrivere un programma che chiede all'utente due numeri interi `a` e `b` (con `a` minore di `b`) e calcola la somma di tutti i numeri interi compresi `a` e `b` (estremi inclusi).

### albero.py

Chiedere in input all'utente un numero `n` forzando l'inserimento di un numero non negativo e stampare un albero di caratteri `*` la cui base contiene un numero di `*` pari ad `n`.

Per esempio inserendo `n = 5` si ottiene:

```
*
**
***
****
*****
```

## Programmi a menu

### calcolatrice.py

Scrivere un programa a menu che simuli il funzionamento di una calcolatrice. L'utente può inserire un comando fra le possibili operazioni (`+`, `-`, `*`, `/`). Successivamente il programma chiede due numeri `a` e `b` e stampa il risultato dell'operazione scelta usando come operandi i numeri forniti.

Per terminare il programma l'utente può inserire l'operando `#`.

### minigiochi.py

Scrivere un programma a menu che permetta all'utente di effettuare a scelta tre diversi minigiochi come descritto di seguito.

1. **Indovina x**: il programma che calcola randomicamente un numero `x` comrpeso fra 0 e 20. Successivamente, il programma valuta una serie di valori inseriti dall'utente e stampa il messaggio *troppo alto* o *troppo basso* per aiutare l'utente a indovinare il numero.
2. **Gara tabelline**: il programma propone all'utente 5 diverse tabelline e, per ciascuna di esse valuta se il risultato è corretto o meno stampando un opportuno messaggio. Il programma stampa anche il totale delle tabelline svolte correttamente dall'utente.
3. **Indovina x difficile**: il programma calcola randomicamente un numero `x` fra 1 e 30 e stampa tutti i valori di cui tale numero è multiplo. Il programma chiede all'utente di indovinare il valore di `x` e stampa un opportuno messaggio di vittoria o sconfitta.
4. **Uscita**