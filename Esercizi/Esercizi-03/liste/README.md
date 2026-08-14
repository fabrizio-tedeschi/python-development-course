# Esercizi 03 - Liste

### iterazione.py

Inizializzare una tupla di 6 frutti. Stampare ogni voce della tupla seguita dal proprio indice di posizione (a partire da 0). Si utilizzi un ciclo `for` per iterare sulla tupla. Viene fornito di seguito un esempio di output.

```
In posizione 0 si trova l'elemento: Mele
In posizione 1 si trova l'elemento: Pere
...
In posizione 5 si trova l'elemento: Ciliege
```

### stampa-pari.py

Scrivere un progrmma che esegua le seguenti operazioni:
* Chieda all'utente di inserire 6 valori numerici in una lista (uno alla volta)
* Crei una nuova lista contenente solo i numeri pari
* Stampi la lista dei numeri pari e la sua lunghezza

### rimuovi-duplicati.py

Scrivere un programma che chiede in input all'utente un valore `n` e successivamente chiede all'utente `n` numeri interi e li inserisce in una lista. Ordinare la lista in ordine decrescente.

Creare una nuova lista senza valori duplicati.

Per esempio se la lista di partenza è `[1, 5, 7, 7, 5, 7, 2]` si otterrà `[7, 5, 2, 1]`.

### statistiche.py

Chiedere in input all'utente un valore `n` e successivamente avviare la procedura di richiesta e inserimento di `n` numeri interi all'interno di una lista.

Stampare successivamente somma, prodotto e media dei numeri contenuti nella lista.

### estremi.py

Riempire una lista con 10 numeri interi random compresi fra -50 e -20. Stampare successivamente il valore massimo e minimo fra gli elementi della lista.

### indovina-numero.py

Scrivere un programma che inserisca in una lista 20 numeri random compresi fra -50 e 50.
Terminata la creazione della lista  il programma chiede all'utente di inserire un valore numerico intero e controlla se questo valore è presente nella lista.
In caso affermativo il programma stampa un messaggio di successo e l'indice a cui si trova l'elemento nella lista. In caso negativo il programma stampa un messaggio di insuccesso.

### ordinamento.py

Siano date le seguenti liste python `l1` ed `l2`:

```python
l1 = ["Mario","Luigi", "Bianca", "Rosa", "Anna"]
l2 = [5, 7, 15, 0, -12, 75, 18]
```

Scrivere un programma che ordini:

* La lista di stringhe `l1` in ordine alfabetico dalla A alla Z (ordine crescente).
* Il programma ordina la lista `l2` in ordine numerico decrescente.

### filtra-parole.py

Si inizializzi la seguente lista:

```python
parole = ["alfabeto", "insuperabile", "", "infinito", "icaro"]
```

Si scriva un programma che crei e stampi una nuova lista contenente solamente le parole che iniziano con i caratteri `"in"`.

**Suggerimento**: sfruttare le tecniche di slicing sulle stringhe.

### substring.py

Si inizializzi la seguente lista:

```python
parole = ["mare", "solemarenuvole", "", "spiaggia", "amarene"]
```

Si scriva un programma che crei e stampi una nuova lista contenente solamente le stringhe che contengono la sequenza di caratteri `"mare"`.

> **Suggerimento**: sfruttare l'operatore `in`.

### task.py

Scrivere un programma che permetta all'utente di gestire una lista di task. Un task è una stringa che descrive una attività da svolgere come ad esempio `"nuoto", "compiti", "calcio"`.

Il programma svolge le seguenti operazioni in ordine:
* Chiede all'utente il numero di task che desidera inserire nella lista
* Chiede all'utente i task da inserire e li inserisce nella lista uno per volta
* Chiede all'utente l'indice di un task da eliminare e lo elimina dalla lista
* Chiede all'utente la stringa di un task da eliminare. Controlla se il task è presente nella lista e in caso affermativo lo elimina. Se il task non è presente nella lista stampa un messaggio di errore.
* Stampa i task restanti uno per volta preceduti dal carattere trattino.

Un esempio di esecuzione del programma potrebbe essere il seguente:

```
Numero di task da inserire: 4
Inserire task: palestra
Inserire task: compiti
Inserire task: nuoto
Inserire task: calcio
Indice di un task da eliminare: 2
Nome di un task da eliminare: basket
ERRORE: task inesistente
Task restanti:
- palestra
- compiti
- calcio
```

### fibonacci.py

La **successione di Fibonacci** è una successione di numeri in cui il numero i-esimo `F(j)` viene definito come `F(j) = F(j-1) + F(j-2)` con la particolarità che `F(0) = 0` e `F(1) = 1`.

Scrivere un programma che chiede in input all'utente un numero intero positivo `n` (forzarne l'inserimento). Il programma calcola e inserisce in una lista tutti i numeri di Fibonacci fino al numero `n`-esimo e poi stampa la lista ottenuta.

Per esempio inserendo `n = 8` si ottiene `[0, 1, 1, 2, 3, 5, 8, 13]` ossia i primi 8 numeri della successione di Fibonacci.

### padovan.py

La **successione di Padovan** è una successione di numeri in cui il numero i-esimo `F(j)` viene definito come `F(j) = F(j-2) + F(j-3)` con la particolarità che `F(0) = 1`, `F(1) = 1` e `F(2) = 1`.

Scrivere un programma che chiede in input all'utente un numero intero positivo `n` (forzarne l'inserimento). Il programma calcola e inserisce in una lista tutti i numeri di Padovan fino al numero `n`-esimo e poi stampa la lista ottenuta.

Per esempio inserendo `n = 10` si ottiene `[1, 1, 1, 2, 2, 3, 4, 5, 7, 9]` ossia i primi 10 numeri della successione di Padovan.

## Liste parallele

### lista-spesa.py

Scrivere un programma che permetta all'utente di gestire una lista della spesa. Il programma svolge le seguenti operazioni in ordine:
* Chiede all'utente il numero di prodotti che desidera inserire nella lista `l`
* Chiede all'utente i prodotti da inserire e li inserisce nella lista uno per volta
* Ordina la lista in ordine alfabetico
* Chiede in input all'utente le quantità che desidera acquistare per ciascun prodotto salvandola in una seconda lista `qt`
* Stampa la lista della spesa stampando un prodotto per volta seguito dalla sua quantità

Un esempio della stampa finale potrebbe essere:

```
Lista della spesa finale:
- Acqua 6
- Banane 2
- Biscotti 10
- Zucchero 1
```

### consumi.py

L'impianto solare di una casa produce energia (misurata in KW) durante le 12 ore di sole di una giornata estiva. Nel contempo la casa consuma energia per via degli elettrodomestici attivi.

Creare e inizializzare le seguenti liste:
* `produzione`: energia prodotta (in KW) per ogni ora. Valori random fra 0 e 15
* `consumi`: consumi della casa (in KW) per ogni ora. Valori random fra 2 e 10.

Per ciascuna ora stampare se la casa sta risparmiando energia, se la casa sta consumando energia, oppure se sta avendo impatto zero (produzione = consumo).

### prezzi.py

Scrivere un programma che chieda in input all'utente il numero `n` di prodotti che desidera inserire. Succesivamente il programma avvia l'inserimento di `n` prodotti (stringhe) chiedendoli in input all'utente e inserendoli in una lista. Forzare l'inserimento di stringhe non vuote.

Il programma genera poi una lista parallela `prezzi` avente `n` elementi, ciascuno calcolato come numero random fra 20 e 300.

Per ciascun prodotto stampare nome, prezzo e fascia di prezzo in base ai seguenti criteri:
* Se il prezzo è inferiore a 50 la fascia è *bassa*
* Se il prezzo è compreso fra 50 e 150 la fascia è *media*
* Se il prezzo è superiore a 150 la fascia è *alta*

### registro.py

Scrivere un programma che simula un registro elettronico scolastico usando tre liste:
* `cognomi`: lista dei cognomi degli studenti
* `classi`: lista delle classi degli studenti
* `medie`: lista delle medie dei voti degli studenti

Le liste contengono nella stessa posizione le informazioni di ciascuno studente. Per esempio accedendo a `cognomi[0]`, `classi[0]` e `media[0]` si ottengono cognome, classe e media dello studente in posizione 0.

Per esempio se si ha:

```python
cognomi = ["Rossi", "Verdi", "Bianchi", "Neri"]
classi = ["2A", "2B", "2A", "2C"]
medie = [6.5, 8.2, 9.1, 6.9]
```

Allora lo studente `Bianchi` appartiene alla classe `2A` e ha una media pari a `9.1`.

Il programma, quando viene avviato, esegue le seguenti operazioni:
1. Chiede all'utente il numero di studenti che vuole inserire.
2. Chiede all'utente le informazioni (cognome, classe e media) di uno studente alla volta e le aggiunge alla rispettive liste.
3. Stampa i cognomi di tutti gli studenti che hanno una media inferiore a 7 preceduti da un opportuno messaggio.
4. Chiede all'utente una classe e stampa i cognomi e le medie di tutti gli studenti appartenenti alla classe fornita.
5. Chiede all'utente un cognome e, dopo aver effettuato gli opportuni controlli, elimina tutti i dati dello studente con quel cognome.

Prima di terminare il programma stampa su output le tre liste.

### calciatori.py

Scrivere un programma a menu che simula un gestore di giocatori di calcio utilizzando tre liste parallele:
* `cognomi`: lista dei cognomi dei giocatori
* `squadre`: lista delle squadre dei giocatori
* `valori_mercato`: lista dei valori di mercato

Le liste contengono nella stessa posizione le informazioni di ciascun calciatore. Per esempio accedendo a `cognomi[0]`, `squadre[0]` e `valori_mecato[0]` si ottengono le informazioni sul primo calciatore.

Il programma a menu deve permettere di effettaure le seguenti operazioni:

1. **Inserimento**: viene richiesto all'utente un numero `n` di calciatori che desidera inserire. Dopo aver richiesto tutti i dati di ciascun calciatore il programma li inserisce nelle rispettive liste.
2. **Filtra squadra**: viene richiesto all'utente il nome di una squadra. Se ci sono calciatori di tale squadra vengono stampati tutti i loro cognomi, altrimenti se non ci sono giocatori per la squadra inserita viene stampato il messaggio *squadra inesistente*.
3. **Soglia valori**: viene richiesta all'utente una soglia `s` (numero intero) e vengono stampati cognome e squadra di ogni giocatore il cui valore di mercato è superiore alla soglia. Forzare l'inserimento di una soglia minima pari a `500`.
4. **Media squadra**: viene richiesto all'utente il nome di una squadra e se la squadra esiste allora viene calcolata e stampata la media dei valori di mercato dei giocatori di tale squadra. Se la squadra non esiste allora viene stampato il messaggio *squadra inesistente*.
5. Uscita e terminazione del programma.

### DOS-attack-defender.py

Un indirizzo IP è una serie di 4 (da 0 a 254) numeri separati da un punto che identifica ciascun dispositivo connesso ad una rete.
Se ne riporta un esempio: `192.50.3.231`.

Un DOS-attack è un attacco informatico che viene messo in atto da un dispositivo che effettua richieste di rete ripetute in un breve lasso di tempo.

Si vuole simulare di seguito un DOS-attack e un sistema di difesa. Si utilizzi:

* Una lista `senders` per raccogliere gli indirizzi IP di tutti i possibili dispositivi che effettuano le richieste (contenente circa 20 indirizzi IP opportunamente generati)
* Una lista `received` per raccogliere gli indirizzi IP che hanno effettuato una o più richieste
* Una lista `blacklist` in cui inserire gli indirizzi IP le cui richieste sono da ignorare

Il programma si comporta come di seguito descritto:

1. Viene scelto casualmente dalla lista `senders` un indirizzo IP
2. Se l'indirizzo IP effettua troppe richieste (compare in `received` più di 4 volte) esso viene aggiunto alla blacklist
3. Se l'indirizzo IP non fa parte della blacklist il programma stampa il messaggio `Fornita risposta ad indirizzo IP: ...`

Tali operazioni vengono ripetute 60 volte (ossia vengono effettuate 60 richieste). Al termine il programma stampa la lista senders e la blacklist.

## Esercizi strutturati

### smartwatch.py

Si veda il testo dell'esercizio al file [smartwatch.md](./smartwatch.md)

### space-station.py

Si veda il testo dell'esercizio al file [space-station.md](./space-station.md)