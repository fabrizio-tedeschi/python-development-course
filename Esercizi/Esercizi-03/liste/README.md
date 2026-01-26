# Esercizi 03 - Liste

### (A) - iterazione.py

Inizializzare una tupla di 6 frutti. Stampare ogni voce della tupla seguita dal proprio indice di posizione (a partire da 0). Si utilizzi un ciclo `for` per iterare sulla tupla. Viene fornito di seguito un esempio di output.

```
In posizione 0 si trova l'elemento: Mele
In posizione 1 si trova l'elemento: Pere
...
In posizione 5 si trova l'elemento: Ciliege
```

### (B) - aggiungi-nomi.py

Scrivere un programma python che chieda in input all'utente 5 nomi e li inserisca all'interno di una lista.
Dopo l'inserimento di ciascun nome il programma stampa il messaggio "DEBUG - inserito nome in posizione x" dove x è l'indice (progressivo) di posizione di ciascun elemento.
Prima di terminare il programma stampa su `stdout` la lista generata.

### (C) - stampa-pari.py

Scrivere un progrmma che esegua le seguenti operazioni:
* Chieda all'utente di inserire 6 valori numerici in una lista
* Crei una nuova lista contenente solo i numeri pari
* Stampi la lista dei numeri pari e la sua lunghezza

### (D) - rimuovi-posizioni-dispari.py

Inizializzare una lista come la seguente:

```python
l = ["Mario", 15, "Luigi", 16, "Bianca", 20, "Rosa", 15, "Anna", 20]
```

Scrivere un programma che sostituisca tutti gli elementi in posizione dispari con una stringa vuota e stampando per ciascuna rimozione il messaggio "DEBUG - rimosso elemento: x" dove x è ciascun valore rimosso.
Prima di terminare il programma stampa la lista e la sua lunghezza dopo le operazioni di rimozione.

### (E) - ordinamento.py

Siano date le seguenti liste python `l1` ed `l2`:

```python
l1 = ["Mario","Luigi", "Bianca", "Rosa", "Anna"]
l2 = [5, 7, 15, 0, -12, 75, 18]
```

Scrivere un programma che ordini:

* La lista di stringhe `l1` in ordine alfabetico dalla A alla Z (ordine crescente).
* Il programma ordina la lista `l2` in ordine numerico decrescente.

> Suggerimento: NON sono necessari algoritmi di ordinamento, sono sufficienti i metodi delle liste.

### (F) - lista-spesa.py

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

### (G) - task.py

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
Inserischi task: palestra
Inserischi task: compiti
Inserischi task: nuoto
Inserischi task: calcio
Indice di un task da eliminare: 2
Nome di un task da eliminare: basket
ERRORE: task inesistente
Task restanti:
- palestra
- compiti
- calcio
```
### (H) - indovina-numero.py

Scrivere un programma che inserisca in una lista 20 numeri random compresi fra -50 e 50.
Terminata la creazione della lista  il programma chiede all'utente di inserire un valore numerico intero e controlla se questo valore è presente nella lista.
In caso affermativo il programma stampa un messaggio di successo e l'indice a cui si trova l'elemento nella lista. In caso negativo il programma stampa un messaggio di insuccesso.

### (I) - DOS-attack-defender.py

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

