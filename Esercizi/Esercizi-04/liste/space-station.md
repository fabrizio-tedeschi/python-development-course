## space-station.py

Una stazione spaziale in orbita raccoglie automaticamente i dati di monitoraggio dell'equipaggio durante una missione di 10 giorni. I dati sono memorizzati nelle seguenti liste:

* `pressione`: pressione atmosferica interna misurata in bar ogni giorno.
* `consumo_ossigeno`: litri di ossigeno consumati dall'equipaggio ogni giorno.
* `anomalie`: numero di anomalie tecniche segnalate dai sistemi ogni giorno.

### Popolamento dei dati

Per popolare le liste procedere come segue:
* Per la pressione inserire valori casuali fra 950 e 1050.
* Per il consumo di ossigeno inserire valori casuali fra 30 e 90.
* Per le anomalie chiedere i valori in input all'utente forzando valori compresi fra 0 e 15.

### Analisi generali

* Stampare il giono con maggior consumo di ossigeno
* Stampare i valori massimo e minimo della pressione in cabina e i rispettivi giorni in cui sono stati registrati
* Stampare il consumo totale di ossigeno dell'intera missione.
* Stampare la media delle anomalie giornaliere
* Stampare in quanti giorni si sono registrate 0 anomalie.

### Analisi avanzate

* Stampare il numero di giorni in cui la pressione è scesa sotto 970 oppure il consumo di ossigeno ha superato i 75 litri.
* Stampaere i giorni (es. 1° giorno, 2° giorno...) in cui ci sono state più di 5 anomalie indicando anche il numero di anomalie registrato.
* Per ciascun giorno stampa una classificazione dello stato di allerta secondo i seguenti criteri:
    * Pressione <960 e anomalie >8: *Critico*
    * Consumo di ossigeno superiore a 70 oppure più di 6 anomalie: *Allerta*
    * Pressione compresa fra 970 e 1030 e anomalie pari o inferiori a 2: *Normale*
    * Tutti gli altri casi: *Da monitorare*

### Dati aggiuntivi

Crea una nuova lista `stress` che per ciascun giorno contenga il prodotto fra il numero di anomalie e il consumo di ossigeno, tutto diviso per la pressione e arrotondato a 2 decimali.

* Stampare il giorno con stress maggiore
* Creare una nuova lista di tuple che contenga, per ogni giorno, una tupla formata come segue `(stress, anomalie)`. Stampare la lista.