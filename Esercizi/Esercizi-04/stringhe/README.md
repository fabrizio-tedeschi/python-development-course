# Esercizi 04 - Stringhe

### inversione.py

Scrivere un programma che chiede in input all'utente una stringa. Il programma genera una nuova stringa che è invertita rispetto all'originale e la stampa.

### conta-vocali.py

Scrivere un programma che chiede in input all'utente una stringa. Il programma conta le vocali presenti nella stringa e stampa il risultato.

### farfallino.py

L'alfabeto farfallino è un gioco in cui ogni vocale di una parola viene raddoppiata aggiundo la lettera f fra la coppia di caratteri. Per esempio la vocale `a` diventa `afa`, la vocale `e` diventa `efe` etc.

Scrivere un programma che chiede all'utente una frase (stringa) e genera e stampa la traduzione della frase in alfabeto farfallino.

Per esempio la frase *"oggi fa caldo"* diventa *"ofoggifi fafa cafaldofo"*.

### conta-parole.py

Scrivere un programma che chiede in input all'utente una frase. Il programma conta le parole presenti nella stringa e stampa il risultato.

### cifre-pari.py

Scrivere un programma che chiede all'utente un numero intero composto da diverse cifre e successivamente stampa solo le cifre pari di tale numero lette da sinistra verso destra separandole con un `-`.

Per esempio inserendo il numero `1234566` viene stampato `2-4-6-6`.

### palindromo.py

Una parola (o una frase) palindroma è una stringa che può essere letta allo stesso modo dall'inizio alla fine oppure dalla fine all'inizio.

Per esempio le parole *ANNA* e *RADAR* e la frase *ANGELA LAVA LA LEGNA* sono palindrome.

Scrivere un programma che chiede in input una stringa (parola o frase) all'utente e, dopo aver rimosso tutti gli spazi e averla resa minuscola, verifica se la stringa è palindroma o meno.

### censura.py
 
Scrivere un programma che chiede in input all'utente una frase e successivamente una parola da censurare. Il programma stampa la frase in cui ogni occorrenza della parola da censurare è stata sostituita da una sequenza di `-` di lunghezza pari a quella della parola.
 
Per esempio inserendo la frase *"il gatto nero è un gatto furbo"* e la parola *"gatto"* viene stampato *"il ---- nero è un ---- furbo"*.

### piu-lunga.py
 
Scrivere un programma che chiede in input all'utente una frase. Il programma stampa la parola più lunga presente nella frase, assieme alla rispettiva lunghezza. In caso di parole di uguale lunghezza si considera la prima incontrata.
 
Per esempio inserendo *"domani vado al mare con Giulia"* si ottiene:
 
```
Parola più lunga: domani (6 caratteri)
```

### indirizzo-mail.py
 
Scrivere un programma che chiede in input all'utente un indirizzo email e verifica se è formalmente valido secondo i seguenti criteri:
* contiene esattamente un carattere `@`;
* il nome utente (la parte prima di `@`) non è vuoto;
* il dominio (la parte dopo `@`) contiene almeno un punto e non inizia né finisce con un punto.

Se l'indirizzo è valido il programma stampa nome utente e dominio separatamente, altrimenti stampa un messaggio di errore.
 
Per esempio inserendo *"mario.rossi@mail.it"* si ottiene:
 
```
Indirizzo valido
Utente: mario.rossi
Dominio: mail.it
```
 
**Suggerimento**: usare `.split("@")` e lo slicing per controllare primo e ultimo carattere del dominio.
 
### password.py
 
Scrivere un programma che chiede in input all'utente una password (forzandone l'inserimento finché non è valida). Una password è valida solo se rispetta **tutti** i seguenti criteri:
* è lunga almeno 8 caratteri;
* contiene almeno una lettera maiuscola;
* contiene almeno una lettera minuscola;
* contiene almeno una cifra.

Se la password non è valida il programma stampa quali criteri non sono stati rispettati. Quando la password è valida stampa `Password accettata`.

### snake-to-camel.py
 
La notazione **snake_case** scrive i nomi composti da più parole in minuscolo separando le parole con un carattere `_` (per esempio `numero_di_studenti`). La notazione **CamelCase** invece unisce le parole eliminando i separatori e scrivendo in maiuscolo la prima lettera di ciascuna parola (per esempio `NumeroDiStudenti`).
 
Scrivere un programma che chiede in input all'utente un nome in notazione snake_case e stampa il corrispondente nome in notazione CamelCase.
 
Per esempio inserendo `numero_di_studenti` viene stampato `NumeroDiStudenti`.
 
**Suggerimenti**:
* Separare le parole con `.split("_")` e ricomporle con `.join()`.
* Per rendere maiuscola solo la prima lettera di una parola combinare lo slicing con il metodo `.upper()`.

### compressione.py
 
La **compressione run-length** è una tecnica che sostituisce ogni sequenza di caratteri consecutivi uguali con il carattere stesso seguito dal numero di ripetizioni.
 
Scrivere un programma che chiede in input all'utente una stringa e stampa la stringa compressa.
 
Per esempio:
* inserendo `aaabbcdddd` viene stampato `a3b2c1d4`;
* inserendo `xyz` viene stampato `x1y1z1`.