# Caos deterministico e mappa logistica

## 1. Introduzione

Il programma Python **caos.py** esplora il comportamento della **mappa logistica**, un modello matematico discreto e non lineare utilizzato per studiare sistemi dinamici che possono evolvere in modo caotico.

L'obiettivo è mostrare due fenomeni:

- **Comportamento caotico:** l'evoluzione della successione numerica può apparire irregolare e imprevedibile.
- **Sensibilità alle condizioni iniziali:** due traiettorie che partono da valori iniziali differenti possono divergere rapidamente, rendendo difficile prevedere il comportamento futuro del sistema.

Questi fenomeni sono esempi di caos deterministico: il sistema segue una legge matematica precisa, ma la sua evoluzione a lungo termine può risultare estremamente sensibile alle condizioni iniziali.

## 2. La formula della mappa logistica

La mappa logistica è definita dalla relazione ricorsiva:

$$
\boxed{x_{n+1}=a\,x_n(1-x_n)}
$$

dove:

- $x_n$ è lo stato del sistema all'iterazione $n$;
- $x_{n+1}$ è lo stato all'iterazione successiva;
- $x_0$ è la condizione iniziale;
- $a$ è il parametro che controlla la dinamica del sistema.

A ogni iterazione, il valore precedente viene inserito nuovamente nella stessa formula per calcolare il valore successivo.

La semplicità dell'equazione è ingannevole: a seconda del parametro $a$, la successione può convergere a un valore stabile, oscillare tra valori periodici oppure entrare in un regime caotico.

## 3. Il regime caotico

Il programma utilizza il parametro:

$$
a=3.97
$$

Questo valore appartiene a una regione in cui la mappa logistica presenta un comportamento caotico per quasi tutte le condizioni iniziali.

Il programma calcola 51 valori della successione, a partire dall'iterazione $n=0$ fino all'iterazione $n=50$.

La prima condizione iniziale è:

$$
x_0=0.5
$$

Applicando la formula si ottiene:

$$
x_1=3.97\cdot0.5\cdot(1-0.5)
$$

e quindi:

$$
x_1=0.9925
$$

Il valore ottenuto viene utilizzato per calcolare $x_2$, e così via.

La successione risultante non converge necessariamente a un singolo valore e presenta oscillazioni irregolari. Il grafico temporale permette di osservare questa evoluzione.

## 4. Sensibilità alle condizioni iniziali

Una delle caratteristiche più importanti dei sistemi caotici è la **sensibilità alle condizioni iniziali**.

In linea di principio, consideriamo due successioni:

$$
x_{n+1}=a\,x_n(1-x_n)
$$

$$
y_{n+1}=a\,y_n(1-y_n)
$$

con condizioni iniziali molto vicine:

$$
x_0\approx y_0
$$

Anche se la differenza iniziale è estremamente piccola, le due successioni possono allontanarsi rapidamente dopo un certo numero di iterazioni.

Indicando con $\Delta_n$ la differenza tra i due valori:

$$
\Delta_n=|x_n-y_n|
$$

nel regime caotico questa differenza può crescere approssimativamente secondo una legge esponenziale:

$$
\Delta_n\approx\Delta_0 e^{\lambda n}
$$

dove:

- $\Delta_0$ è la differenza iniziale;
- $\lambda$ è l'esponente di Lyapunov;
- $n$ è il numero di iterazioni.

Quando l'esponente di Lyapunov è positivo, piccole differenze iniziali tendono a essere amplificate nel tempo, almeno in una prima fase della divergenza.

Questo fenomeno è spesso associato all'**effetto farfalla**, espressione utilizzata per descrivere come piccole variazioni nelle condizioni iniziali possano produrre grandi differenze nell'evoluzione di un sistema dinamico.

## 5. Struttura del programma

Il programma utilizza Python e tre moduli:

- `numpy`, per memorizzare e calcolare le successioni numeriche;
- `matplotlib`, per generare i grafici;
- `random`, per generare una condizione iniziale casuale.

### 5.1 Generazione di una condizione iniziale casuale

La funzione `delta_casuale()` restituisce un numero compreso tra $0$ e $0.999999$:

```python
def delta_casuale():
    return random.randint(0, 999_999) / 1_000_000
```

Il valore viene utilizzato come seconda condizione iniziale.

### 5.2 Calcolo della mappa logistica

La funzione `mappa_logistica(a, x0, n_passi)` calcola la successione:

```python
def mappa_logistica(a, x0, n_passi):
    """Calcola la sequenza della mappa logistica."""
    x = np.zeros(n_passi)
    x[0] = x0

    for i in range(1, n_passi):
        x[i] = a * x[i-1] * (1 - x[i-1])

    return x
```

Il funzionamento è semplice:

1. Viene creato un array di `n_passi` elementi inizializzati a zero.
2. Il primo elemento viene impostato al valore iniziale `x0`.
3. Un ciclo calcola ogni valore successivo utilizzando quello precedente.
4. La funzione restituisce l'intera successione.

### 5.3 Parametri della simulazione

I parametri principali sono:

```python
a = 3.97
n_passi = 51

x0_a = 0.5
x0_b = delta_casuale()
```

Il programma genera quindi due successioni indipendenti, utilizzando lo stesso parametro $a$ ma condizioni iniziali differenti.

## 6. Interpretazione dei grafici

Il programma produce una figura contenente due grafici.

### Grafico 1 — Evoluzione temporale

Il primo grafico mostra la successione generata a partire da:

$$
x_0=0.5
$$

L'asse orizzontale rappresenta il numero di iterazioni $n$, mentre l'asse verticale rappresenta il valore $x_n$.

Le oscillazioni irregolari illustrano il comportamento della mappa logistica nel regime caotico.

### Grafico 2 — Confronto tra due traiettorie

Il secondo grafico sovrappone le due successioni:

- la prima, con condizione iniziale $x_{0,a}=0.5$;
- la seconda, con condizione iniziale scelta casualmente.

Il confronto permette di osservare come due condizioni iniziali diverse producano traiettorie differenti.

**Nota importante:** nella versione attuale del programma, la seconda condizione iniziale viene estratta casualmente da un intervallo molto ampio. Pertanto, i due valori iniziali non sono necessariamente vicini. Il grafico mostra la differenza tra due traiettorie, ma non dimostra da solo la sensibilità a perturbazioni infinitesime.

Per osservare più chiaramente l'effetto delle condizioni iniziali, è possibile sostituire:

```python
x0_b = delta_casuale()
```

con:

```python
x0_b = 0.500001
```

In questo modo, le due successioni partono da valori molto vicini:

$$
x_{0,a}=0.5
$$

$$
x_{0,b}=0.500001
$$

La differenza iniziale è:

$$
\Delta_0=10^{-6}
$$

Confrontando le due traiettorie si può osservare come una perturbazione iniziale molto piccola possa amplificarsi nel corso delle iterazioni.

## 7. Caos deterministico e imprevedibilità

Il comportamento caotico non significa che il sistema sia privo di regole.

La mappa logistica è completamente deterministica: se il parametro e la condizione iniziale sono gli stessi, la successione matematica è la stessa.

L'imprevedibilità pratica nasce dalla sensibilità alle condizioni iniziali. Anche errori di misura o piccole imprecisioni nella rappresentazione numerica possono rendere difficile prevedere con precisione l'evoluzione a lungo termine.

È inoltre importante distinguere il caos deterministico dalla casualità autentica: la successione viene generata da una formula matematica, non da un processo casuale a ogni iterazione.

## 8. Conclusioni

Questo esperimento mostra come una semplice equazione non lineare possa produrre dinamiche complesse.

La mappa logistica costituisce un modello didattico utile per comprendere:

- i sistemi dinamici discreti;
- le successioni ricorsive;
- il comportamento caotico;
- la sensibilità alle condizioni iniziali;
- il concetto di imprevedibilità nei sistemi deterministici.

La possibilità di modificare il parametro $a$, la condizione iniziale e il numero di iterazioni rende il programma uno strumento semplice per esplorare numericamente alcuni dei concetti fondamentali della teoria del caos.
