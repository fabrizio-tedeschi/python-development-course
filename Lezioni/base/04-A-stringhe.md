# Stringhe

Le **stringhe**, finora trattate come dato semplice alla pari dei numeri interi, sono in realtà strutture complesse che possono essere utilizzate come strutture dati. Perciò, è possibile iterare su una stringa:

```python
s = "ciao"

for ch in s:
    print(ch)
```

## Operazioni elementari

Si possono confrontare le stringhe con gli operatori `>` e `<` che permettono di verificare l'ordine alfabetico. Più precisamente **una stringa è minore di un'altra se viene prima secondo l'ordine alfabetico**.

```python
s0 = "zebra"
s1 = "micio"
s2 = "micione"

print(s0 < s1)      # False: zebra viene dopo micio
print(s0 > s1)      # True: zebra viene dopo micio
print(s1 < s2)      # True: micio alfabeticamente viene prima di micione
```

Si possono concatenare le stringhe tramite l'operatore `+`. Poichè le stringhe sono **immutabili** l'operatore `+` restituisce una nuova stringa che è il risultato della concatenazione delle due iniziali.

```python
s1 = "ciao"
s1 = "mare"
s3 = s1 + " " + s2

print(s3)      # Stampa: 'ciao mare'
```

## Funzioni che si applicano sulle stringhe

Le seguenti funzioni possono accettare una stringa come argomento:

* `len()`: ritorna la lunghezza della stringa
* `max()`: ritorna la lettera dell'alfabeto della stringa più vicina alla `z`.
* `min()`: ritorna la lettera dell'alfabeto della stringa più vicina alla `a`.

```python
s = "ciao"

print(len(s))           # Stampa: 4
print(max(s))           # Stampa: o
print(min(s))           # Stampa: a
```

## Metodi delle stringhe

Come tutte le strutture dati, anche le stringe possiedono metodi, se ne riportano alcuni

* `.isalpha()`: Restituisce `True` se la stringa contiene solo caratteri alfabetici;
* `.isdecimal()`: Restituisce `True` se la stringa contiene solo caratteri numerici;

* `.isupper()`: Restituisce `True` se la stringa contiene solo caratteri maiuscoli;
* `.islower()`: Restituisce `True` se la stringa contiene solo caratteri minuscoli;

* `.upper()`: Restituisce la stessa stringa ma con tutti i caratteri in maiuscolo;
* `.lower()`: Restituisce la stessa stringa ma con tutti i caratteri in minuscolo;

* `.replace(old, new)`: Restituisce una nuova stringa in cui ogni occorrenza di `old` viene sostituita con `new`;

## Slicing di stringhe

Si dice *slicing* l'operazione di "taglio" di una stringa considerando solamente una certa sua parte. In python è possibile effettuare lo slicing di stringe tramite la sintassi `string[start:end]` dove `start` e `end` sono indici di un intervallo di caratteri della stringa.

```python
str = "abcdefgh..."

sliced = str[2:]                #cdefgh...
sliced = str[2:5]               #cde
sliced = str[:5]                #abcde
sliced = str[-3:]               #...
sliced = str[:-3]               #abcdefgh
```

**NB**: gli indici seguono la logica *primo incluso, ultimo escluso*.

## Passaggio da liste a stringhe

I metodi seguenti permettono di convertire stringhe in liste e viceversa:
* `.split(ch)`: Restituisce una lista in cui ogni elemento è una parte della stringa che viene separata ogni volta che si incontra il carattere `ch`;
* `sep.join(ls)`: Restituisce una stringa composta da ciascuno degli elementi della lista `ls` separati dalla stringa separatore `sep` su cui viene invocata;

```python
l = ["Oggi", "fuori", "piove"]
out = " ".join(l)                   #out = "Oggi fuori piove"
div = out.split(" ")                #div = ["Oggi", "fuori", "piove"]
```