# Esercizi con strutture dati miste

### posizioni-estremi.py
 
Chiedere in input all'utente un valore `n` e successivamente `n` numeri interi, inserendoli in una lista.
 
Costruire e stampare una tupla `(minimo, indice_minimo, massimo, indice_massimo)`. In caso di valori ripetuti considerare la prima occorrenza.
 
Per esempio con la lista `[4, 9, 1, 9, 3]` si otterrà `(1, 2, 9, 1)`.

### esami.py
 
Si consideri la seguente lista di tuple che contiene gli esami sostenuti da uno studente:
 
```python
esami = [("analisi", 27), ("fisica", 18), ("informatica", 30), ("algebra", 24)]
```
 
Stampare, nell'ordine:
- Il nome dell'esame con il voto più alto
- La media dei voti

### anagrafica.py
 
Chiedere in input all'utente un valore `n` e successivamente, per `n` volte, nome ed età di una persona. Memorizzare ogni persona come tupla `(nome, età)` all'interno di una lista.
 
Stampare successivamente:
 
- Nome e età della persona più giovane
- L'età media

### punti-casuali.py
 
Riempire una lista con 8 punti, ciascuno rappresentato da una tupla `(x, y)` con coordinate intere random comprese fra -10 e 10.
 
Stampare successivamente:
 
- L'elenco dei punti
- I soli punti che si trovano nel primo quadrante, cioè con `x` e `y` entrambe positive

### magazzino.py
 
Si consideri la seguente lista di tuple:
 
```python
magazzino = [("viti", 120, 0.05), ("bulloni", 4, 0.20), ("chiodi", 300, 0.02), ("rondelle", 3, 0.10)]
```
 
Stampare successivamente:
 
- Il valore totale del magazzino, cioè la somma di quantità per prezzo di ogni prodotto
- I soli nomi dei prodotti con quantità inferiore a 5