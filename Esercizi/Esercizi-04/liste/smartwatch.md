## smartwatch.py

Uno smartwatch di ultima generazione ha collezionato i dati di allenamento di un atleta durante la settimana (7 giorni) all'interno delle seguenti liste:
* `battiti_cardiaci`: contiene la frequenza cardiaca dell'atleta di ogni giorno
* `minuti`: contiene i minuti di allenamento effettuati ciascun giorno
* `fatica`: contiene un indicatore di fatica (numero intero fra 1 e 10) dell'altleta ciascun giorno.

### Popolamento dei dati

Per popolare le liste procedere come segue:
* Per i battiti cardiaci inserire valori casuali fra 80 e 150
* Per i minuti inserire valori casuali fra 50 e 180
* Per i valori di fatica di ciascuna giornata, chiederli all'utente. Forzare l'inserimento di valori compresi fra 1 e 10.

### Analisi generali

* Stampare il giorno in cui è stato effettauto il maggior numero di minuti di allenamento (es. *Giorno 1* oppure *Giorno 2*...)
* Stampare il valore minore di battiti cardiaci e il giorno in cui è stato registrato.
* Stampare il totale dei minuti di allenamento della settimana
* Stampare la media dei battiti cardiaci della settimana

### Analisi avanzate

* Stampare il numero di giorni per i quali la frequenza cardiaca ha superato il valore 120 oppure il numero di minuti di allenamento è stato superiore a 90.
* Stampare tutti i giorni nei quali l'utente ha registrato un livello di fatica superiore a 7.
* Per ciascun giorno stampa una classificazione dell'allenamento svolto come di seguito indicato:
    * Battiti inferiori a 100 o fatica inferiore a 5: *Leggero*
    * Minuti superiori a 120 o fatica superiore a 6: *Medio*
    * Battiti superiori a 120 e fatica superiore o uguale a 7: *Pesante*

### Dati aggiuntivi

Crea una nuova lista `efficienza` che per ciascun giorno contiene il rapporto fra i battiti cardiaci e il livello di fatica.

Per ogni giorno creare e stampare una tupla definita come segue `(giorno, battiti, efficienza)`. Il primo valore della tupla è l'indice del giorno di allenamento, i valori seguenti sono i corrispondeti valori di battiti_cardiaci ed efficienza di quel giorno.