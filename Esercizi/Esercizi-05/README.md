# Esercizi 05 - File di testo

### readlines.py

Dato il file di testo `files/primo.txt` scrivere un programma che legga le prime 10 righe e le stampi su `stdout`.

### duplica.py

Scrivere un programma che legga tutte le linee del file `files/primo.txt` e le scriva all'interno del file `files/duplica-out.txt`.

### printonfile.py

Scrivere un programma che chieda in input all'utente 10 linee di testo e le inserisca in un file `files/print-out.txt`.

### indice-linee.py

Scrivere un programma che legga ciascuna linea del file `files/primo.txt` e la stampi su `stdout` preceduta dal suo indice di linea
come mostrato di seguito.

```
Linea_1: File di tetso primo.txt
Linea_2: Seconda linea del file
...
```

### conta-parole.py

Dato il file `files/secondo.txt` scrivere un programma che chieda all'utente di inserire una parola e stampi su `stdout` il numero
di volte in cui la parola passata compare all'interno del file.

> **Suggerimento**: si veda il funzionamento del metodo delle stringhe .split() e lo si applichi opportunamente al programma.

### file-numerico.py

Dato il file `files/numeri.txt` si scriva un programma che esegue le seguenti operazioni:
* Stampa la media della sequenza di numeri contenuta nel file
* Stampa massimo e minimo della sequenza di numeri contenuta nel file

**Complicazione**: anzichè stampare i risultati su terminale, inserirli all'interno di un nuovo file nominato `risultati.txt`.

### dati-calciatori.py

Si consideri il file `calciatori.csv` che contiene un elenco di cognomi di calciatori e i goal effettuati in diverse partite.

Scrivere un programma che:
* Stampa il totale dei goal per ogni calciatore
* Stampa il cognome del calciatore che ha effettuato più goal