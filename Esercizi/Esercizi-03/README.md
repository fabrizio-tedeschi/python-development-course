# Esercizi 03 - Strutture dati

## Liste

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

### (C) - rimuovi-dispari.py

Sia data la seguente lista python con **stringhe in posizioni pari e interi in posizioni dispari**:

```python
l = ["Mario", 15, "Luigi", 16, "Bianca", 20, "Rosa", 15, "Anna", 20]
```

Scrivere un programma che rimuova dalla lista tutti i numeri interi sostituendoli con una stringa vuota e stampando per ciascuna rimozione il messaggio "DEBUG - rimosso elemento: x" dove x è ciascun valore rimosso.
Prima di terminare il programma stampa la lista "sfoltita" su `stdout` e la sua dimensione/lunghezza.

### (D) - ordinamento.py

Siano date le seguenti liste python `l1` ed `l2`:

```python
l1 = ["Mario","Luigi", "Bianca", "Rosa", "Anna"]
l2 = [5, 7, 15, 0, -12, 75, 18]
```

Scrivere un programma che ordini:

* La lista di stringhe `l1` in ordine alfabetico dalla A alla Z (ordine crescente).
* Il programma ordina la lista `l2` in ordine numerico decrescente.

> Suggerimento: NON sono necessari algoritmi di ordinamento, sono sufficienti i metodi delle liste.

### (E) - indovina-numero.py

Scrivere un programma che inserisca in una lista 20 numeri random compresi fra -50 e 50.
Terminata la creazione della lista  il programma chiede all'utente di inserire un valore numerico intero e controlla se questo valore è presente nella lista.
In caso affermativo il programma stampa un messaggio di successo e l'indice a cui si trova l'elemento nella lista. In caso negativo il programma stampa un messaggio di insuccesso.

### (F) - DOS-attack-defender.py

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

## Dictionary

### (G) - prodotti.py

Inizializzare un dictionary vuoto `prodotti`. Ciascuna chiave di tale dictionary è costituita da un intero progressivo maggiore di 1,
ciascun valore da una stringa che contiene il nome di un prodotto di un supermercato.

Si chieda all'utente di inserire 10 prodotti e successivamente si stampi ciascun prodotto (valore) assieme al proprio codice associato (chiave).

### (H) - estrazione-chiavi.py

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

### (I) - estrazione-coppie.py

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

### (L) - nuotatori.py

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

### (M) - classifica-nuotatori.py

Inizializzare una lista `nuotatori` con 4 dictionary contenenti i dati mostrati nella tabella dell'esercizio precedente.

Stampare la classifica dei nuotatori posizionando coloro che hanno effettuato il miglior tempo in alto.

La classifica deve avere il seguente formato di stampa:
 ```
 1. Bianchi - 80 - Stile
 2. Verdi - 110 - Rana
 ```

Stampare in modo analogo la classifica dei soli nuotatori con stile `Free`.

*Suggerimento*: per prima cosa è necessario riordinare la lista per miglior tempo. Successivamente la si scorre tutta e si procede alla stampa con le posizioni in classifica.