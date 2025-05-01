# Strutture dati

Si dice **struttura dati** una entità utilizzata per organizzare un insieme di dati legati da un certo tipo di relazione. In python sono presenti le seguenti strutture dati:

* `Liste`: insiemi di elementi.
* `Tuple`: insiemi immutabili di elementi.
* `Set`: insiemi di elementi immutabili e non ordinati.
* `Dictionary`: insieme di elementi (valori) identificati da una corrispondente parola (chiave).

>[!TIP]
> **Iterazione su strutture dati** 
> 
> Tutte le strutture dati sono oggetti sui quali è possibile eseguire iterazioni. Ciò significa che esse possono essere inserite al'interno di un ciclo `for` nel quale la variabile assumerà via via il valore di ciascun elemento della strututra dati.

```python
#Operazioni iniziali

for elemento in struttura_dati:
    #Operazioni da eseguire durante ciascuna iterazione

#Operazioni successive
```

## Stringhe come strutture dati

Le stringhe, finora trattate come dato semplice alla pari dei numeri interi, sono in realtà strutture complesse che possono
essere utilizzate come strutture dati. Perciò, è possibile iterare su una stringa:

```python
str = "ciao"

for ch in str:
    print(ch)
```

Per ricavare la lunghezza di caratteri contenuti in una stringa è possibile utilizzare la funzione `len(mystring)`.

### Metodi delle stringhe

Come tutte le strutture dati, anche le stringe possiedono metodi, se ne riportano alcuni

* `.isalpha()`: Restituisce `True` se la stringa contiene solo caratteri alfabetici;
* `.isdecimal()`: Restituisce `True` se la stringa contiene solo caratteri numerici;

* `.upper()`: Restituisce la stessa stringa ma con tutti i caratteri in maiuscolo;
* `.lower()`: Restituisce la stessa stringa ma con tutti i caratteri in minuscolo;

* `string.split()`: Restituisce una lista in cui ogni elemento è una parola della stringa;
* `list.join()`: Restituisce una stringa composta da ciascuno degli elementi della lista separati da spazi;

```python
l = ["Oggi", "fuori", "piove"]
out = l.join()                      #out = "Oggi fuori piove"
div = out.split()                   #div = ["Oggi", "fuori", "piove"]
```

* `.format(p1, p2, ...)`: Permette di definire campi variabili in una stringa e formattarla con i parametri passati;

```python
str = "Parte fissa della stringa seguita da un campo: {}"
print(str.format("Campo X"))                #Stampa: "Parte fissa della stringa seguita da un campo: Campo X"

nome = "MARIO"
print(str.format(nome))               #Stampa: "Parte fissa della stringa seguita da un campo: MARIO"
```

### Slicing di stringhe

Si dice *slicing* l'operazione di "taglio" di una stringa considerando solamente una certa sua parte. In python è possibile effettuare
lo slicing di stringe tramite la sintassi `string[start:end]` dove `start` e `end` sono indici di un intervallo di caratteri della stringa.

```python
str = "abcdefgh..."

sliced = str[2:]                #cdefgh...
sliced = str[2:5]               #def
sliced = str[:5]                #abcde
sliced = str[-3:]               #...
sliced = str[:-3]               #abcdefgh
```

## Tuple

Le tuple sono insiemi IMMUTABILI di elementi. Ciò significa che esse vengono inizializzate e non possono essere modificate successivamente.

```python
#Definizione di una tupla
colori = ("rosso", "verde", "blue", "giallo")
```

## Liste

Le liste python sono insiemi che possiedono le seguenti caratteristiche:

* Gli elementi contenuti nella lista sono disposti in un certo ordine (casuale o definito)
* Gli elementi contenuti nella lista possono essere tipi di dato differenti
* Gli elementi contenuti nella lista possono essere ripetuti
* La lista è una struttura dati variabile nel tempo (può subire modifiche)

```python
#Definizione di una lista vuota
empty_list = []

#Inizializzazione di una lista
my_list = ["Mario", 15, "Mele", "Pere", 37]

#Stampa delle liste
print(empty_list)
print(my_list)
```

>[!NOTE]
> Poichè le liste python non pongono limiti ai tipi di elemento in esse contenuti una lista può contenere altre liste.

```python
#Inizializzazione di una lista composta da liste di due elementi ciascuna
coppie = [[1, 2], [10, 20], [100, 200]]
```

### Accesso agli elementi della lista

Per accedere agli elementi di una lista è possibile utilizzare l'operatore `[]` posto al termine del nome di una lista.

>[!TIP]
> Tutte le strutture dati sono di tipo 0-based, ciò significa che il primo elemento occupa posizione zero!

![lista](./images/lista.jpg)

```python
#Inizializzazione di una lista di numeri
dispari = [1, 3, 5, 7, 9]

print(dispari[0])           #Stampa: 1
print(dispari[1])           #Stampa: 3
print(dispari[-1])          #Stampa: 9
```

Per modificare gli elementi di una lista è possibile utilizzare l'operatore di assegnazione `=`:

```python
#Inizializzazione di una lista di numeri
l = [1, 2]

#Modifica del secondo elemento
l[1] = 50
print(l)                    #Stampa: [1, 50]
```

Nel caso si voglia accedere a ciascun elemento della lista ed effettuare operazioni su di esso, allora risulta opportuno un ciclo `for` per iterare sulla lista:

```python
#Inizializzazione di una lista di numeri
dispari = [1, 3, 5, 7, 9]

#Stampa di ciascun elemento moltiplicato per 10
for e in dispari:
    print(e * 10)
```

### Metodi dell liste

I **metodi** sono funzioni proprie delle liste che permettono di modificarle (alterarne la struttura). Essi si applicano alla variabile che identifica la lista tramite l'operatore punto: `.nome_metodo()`

* `.append(e)`: permette di aggiungere l'elemento `e` in coda alla lista;
* `.insert(i, e)`: permette di aggiungere l'elemento `e` nella posizione di indice `i` della lista;
* `.pop(i)`: permette di rimuovere l'elemento all'indice `i` dalla lista e lo restituisce;
* `.remove(e)`: permette di rimuovere l'elemento `e` dalla lista;
* `.index(e)`: restituisce l'indice della prima occorrenza di `e` nella lista;
* `.sort()`: ordina la lista secondo il normale ordine crescente (per elementi dello stesso tipo);
* `.reverse()`: inverte l'ordine degli elementi della lista;
* `.count(e)`: restituisce il numero di occorrenze di `e` presenti nella lista;

```python
#Definizione di una lista vuota
l = []

#Aggiunta di tre elementi
l.append(3)
l.append("parola")
l.append(50)

#Inserimento di un elemento in posizione 1
l.insert(1, 5)

#Rimozione della stringa
l.remove("parola")

#Rimozione del primo elemento
popped = l.pop(0)

print(popped)               #Stampa: 3
print(l)                    #Stampa: [5, 50]
```

## Dictionary

I dictionary sono insiemi di coppie chiave-valore in cui ciascuna chiave è associata al corrispondente valore.

* Ciascuna *chiave* è un elemento immutabile (stringa o intero che sia)
* Ciacun *valore* è un elemento che può essere un numero, una stringa, una lista, una tupla o un'altro dictionary

```python
#Creazione di un dictionary vuoto
empty_dict = {}
```

### Accesso agli elementi di un dictionary

Per accedere agli elementi di una lista è possibile utilizzare l'operatore `[]` posto al termine del nome del dictionary.

```python
#Definizione di un dictionary per rappresentare una persona
persona_uno = {
    "nome": "Mario",
    "cognome": "Rossi",
    "Anni": 25,
    "colori_preferiti": ["blu", "verde"],
    "Studente": True
}

#Stampa di nome, cognome e anni
print("Dati anagrafici:", persona_uno["nome"], persona_uno["cognome"], persona_uno["anni"])
```

>[!WARNING]
> In caso si tenti di accedere a un valore tramite una chiave inesistente si ottiene un `KeyError`, errore che interrompe il programma.
> Per evitare tale errore è possibile ricorrere al metodo `.get(k, other)` che ritorna il valore associato alla chiave `k` oppure l'elemento `other` oppure `None` (il vuoto) in caso il secondo parametro non sia specificato.

```python
#Definizione di un dictionary
my_dict = {
    "k1": "Mele",
    "k2": "Pere"
}

#Utilizzo del metodo get
print(my_dict.get("k1"))                            #Stampa: Mele
print(my_dict.get("k3"))                            #Stampa: None
print(my_dict.get("k3", "Chiave inesistente"))      #Stampa: chiave inesistente
```

### Modifica degli elementi e aggiunta di nuove chiavi

```python
#Definizione di un dictionary
prodotti  = {
    156: "Oro",
    157: "Argento",
    158: "Bronzo"
}

#Aggiunta di una chiave
prodotti[159] = "Alluminio"

#Modifica di un elemento
prodotti[158] = "Rame"
```

### Iterazione su dictionary

I dictionary python possiedono i seguenti metodi:

* `.keys()`: restituisce le chiavi del dicionay come lista
* `.values()`: restituisce i valori del dicionay come lista
* `.items()`: restituisce una lista di tuple di due elementi (chiave-valore)

```python
#Definizione di un dictionary
my_dict = {
    "k1": "Mele",
    "k2": "Pere"
}

keys = my_dict.keys()           #Restituisce: ["k1", "k2"]
values = my_dict.values()       #Restituisce: ["Mele", "Pere"]
items = my_dict.items()         #Restituisce: [("k1", "Mele"), ("k2", "Pere")]
```

Per iterare sugli oggetti di un dictionary è possibile utilizzare una coppia di variabili come mostrato nel seguito:

```python
#Iterazione su oggetti di un dictionary
for k, v in my_dict.items():
    #Operazioni da svolgere durante ciascuna iterazione

#Operazioni successive
```