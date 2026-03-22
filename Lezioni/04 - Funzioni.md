# Funzioni

Una **funzione** è una unità di organizzazione del codice. Essa permette di raggruppare in un unico blocco caratterizzato da
un nome un insieme di istruzioni.

```
#Definizione di una funzione
def nome_funzione(parametri):
    Istruzioni
    return valore_da_restituire
```

Per eseguire l'insieme di istruzioni è possibile **chiamare** o **invocare** la funzione tramite il proprio nome.

```
#Chiamata di una funzione
nome_funzione(parametri)
```

Una funzione può svolgere le operazioni in essa contenute utilizzando una serie di valori a essa forniti detti **parametri**.

Una funzione può fornire un **valore di ritorno** che può essere salvato in una variabile. Solitamente esso è il risultato prodotto dalle istruzioni eseguite.

```
#Chiamata di una funzione e salvataggio valore di ritorno
risultato = nome_funzione(parametri)
```

>[!TIP]
> #### Domande utili da porsi prima di definire una funzione
> In sede di definizione o utilizzo di una funzione è sempre buona norma riuscire a rispondere alle seguenti domande:
> * Come si chiama?
> * Che cosa fa?
> * Quali parametri accetta?
> * Cosa restituisce

### Definizione di una funzione

```python
#Definizione della funzione
def nome_funzione(par1, par2, par2):
    #Istruzioni della funzione...
    return risultato

#Chiamata della funzione
x = 7
res = nome_funzione(1, "Mario", x)
```

Di seguito un esempio di una funzione che saluta l'utente:

```python
def saluta(nome):
    print("Buongiorno!", nome)

#Chiamata della funzione
saluta("Mario")                     #Stampa: Buongiorno! Mario
saluta("Genoveffa")                 #Stampa: Buongiorno! Genoveffa
```

>[!NOTE]
> Il linguaggio Python non pone vincoli sul tipo dei parametri (interi, stringhe, liste...) TUTTAVIA se un parametro viene
> considerato essere di un certo tipo è bene che esso venga passato in base al tipo predisposto dalla progettazione!
>
> ```python
> def aggiungi_elemento(lista, elemento):
>   lista.append(elemento)
>   return lista
> 
> l = [1, 2, 3]
> l = aggiungi_elemento(l, 4)               #Ritorna: [1, 2, 3, 4]
> l = aggiungi_elemento(l, 5)               #Ritorna: [1, 2, 3, 4, 5]
> nuova = aggiungi_elemento(75, 2)          #ERRORE: il valore 75 non possiede il metodo .append()
> ```

## Passaggio per copia e per riferimento

Quando una variabile viene passata come parametro di una funzione, il suo contenuto può essere passati:

* Per **COPIA**: il contenuto della variabile viene copiato in una nuova variabile e successivamente usato dalla funzione;
* Per **RIFERIMENTO**: viene conservato un riferimento al dato in memorie e questo viene modificato ovunque;

Si consideri il seguente esempio:

```python
def aggiungi(x):
    return x + 10                           #Ritorna: x + 10

def aggiungi_elemento(lista, elemento):
    lista.append(elemento)                  #Aggiunge l'elemento alla lista l
    return lista                            #Ritorna un nuovo riferimento alla lista l

var = 15
l = [1, 2, 3]

res = aggiungi(var)
print(var)                                  #Stampa: 15
print(res)                                  #Stampa: 25

risultato = aggiungi_elemento(l, 4)
risultato.append(5)

print(l)                                    #Stampa: [1, 2, 3, 4, 5]
print(risultato)                            #Stampa: [1, 2, 3, 4, 5]
```

>[!TIP]
> In python numeri e stringhe sono passati per copia, liste e dictionary sono passati per riferimento.

## Valori di default

Talvolta una funzione necessita di un certo parametro per svolgere il proprio compito ma non sempre è possibile passarlo.
Per ovviare a tale problema vengono utilizzati parametri con valori di default.

Per impostare un valore di default di un parametro si utilizza l'operatore `=` al momento della definizione della funzione:

```python
def saluta(nome, messaggio = "Ciao,"):
    print(messaggio, nome)

saluta("Mario", "Benvenuto!")               #Stampa: Benvenuto! Mario
saluta("Mario")                             #Stampa: Ciao, Mario
```

>[!NOTE]
> Dato che i parametri di una funzione vengono passati IN ORDINE è sempre bene porre i parametri opzionali come ultimi parametri dell'elenco.

## Approccio top-down

L'approccio **top-down** in informatica è una metodologia che consiste nel suddividere un problema complesso (dall'alto) in sotto-problemi più semplici (verso il basso).

L'approccio top-down viene realizzato all'interno dei programmi suddividendo un compito esteso e complesso in sotto-compiti semplici svolti da funzioni differenti.

Una volta definite le diverse funzioni che risolvono i sotto-problemi una funzione principale solitamente detta `main()` si occuperà di chiamarle nell'ordine più opportuno.

*Esempio*: si vuole scrivere un programma che permette di gestire ordini online di alcuni utenti. Quando un utente effettua un ordine il processo di gestione è il seguente:
1. Viene chiesto all'utente quali prodotti desidera acquistare e questi vengono inseriti nel carrello
2. Viene calcolato il totale del carrello
3. Viene effettuato il pagamento
4. Viene aggiornato l'inventario

Una possibile implementazione del programma potrebbe essere la seguente:

```python
# Definizione delle funzioni base
def inserimento_prodotti():
    # ...

def calcola_totale_carrello():
    # ...

def paga():
    # ...

def aggiorna_inventario():
    # ...

# Funzione principale (che chiama le altre)
def main():
    inserimento_prodotti()
    calcola_totale_carrello()

    pagato = paga()
    if(pagato == True):
        agggiorna_inventario()

# Inizio del programma chiamando la funzione principale
main()
```
